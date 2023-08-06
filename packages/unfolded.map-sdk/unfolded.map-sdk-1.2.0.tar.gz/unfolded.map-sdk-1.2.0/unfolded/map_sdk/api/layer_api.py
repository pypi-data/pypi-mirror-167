from abc import abstractmethod
from typing import Any, Callable, Dict, List, Optional, Union

from pydantic import StrictBool, StrictStr

from unfolded.map_sdk.api.base import Action, CamelCaseBaseModel, Number, TimeRange
from unfolded.map_sdk.api.enums import ActionType, LayerType
from unfolded.map_sdk.transport.base import (
    BaseInteractiveTransport,
    BaseNonInteractiveTransport,
)
from unfolded.map_sdk.utils.validators import validate_kwargs


class VisualChannel(CamelCaseBaseModel):
    name: StrictStr
    type: StrictStr


VisualChannels = Dict[StrictStr, Union[VisualChannel, StrictStr, None]]


class _PartialLayerConfig(CamelCaseBaseModel):
    visual_channels: Optional[VisualChannels]
    """Dictionary of visualization properties that the layer supports."""

    vis_config: Optional[Dict[StrictStr, Any]]
    """General layer settings."""


class LayerConfig(_PartialLayerConfig):
    visual_channels: VisualChannels
    """Dictionary of visualization properties that the layer supports."""

    vis_config: Dict[StrictStr, Any]
    """General layer settings."""


class _LayerUpdateProps(CamelCaseBaseModel):
    type: Optional[LayerType]
    """Type of the layer."""

    data_id: Optional[StrictStr]
    """Unique identifier of the dataset this layer visualizes."""

    fields: Optional[Dict[StrictStr, Optional[StrictStr]]]
    """Dictionary that maps fields that the layer requires for visualization to appropriate dataset fields."""

    label: Optional[StrictStr]
    """Canonical label of this layer."""

    is_visible: Optional[StrictBool]
    """Flag indicating whether layer is visible or not."""

    config: Optional[_PartialLayerConfig]
    """Layer configuration specific to its type."""


class _LayerCreationProps(_LayerUpdateProps):
    id: Optional[StrictStr]
    """Unique identifier of the layer."""

    type: Optional[LayerType]
    """Type of the layer."""

    data_id: StrictStr
    """Unique identifier of the dataset this layer visualizes."""

    fields: Optional[Dict[StrictStr, Optional[StrictStr]]]
    """Dictionary that maps fields that the layer requires for visualization to appropriate dataset fields."""

    label: Optional[StrictStr]
    """Canonical label of this layer."""

    is_visible: Optional[StrictBool]
    """Flag indicating whether layer is visible or not."""

    config: Optional[_PartialLayerConfig]
    """Layer configuration specific to its type."""


class Layer(_LayerCreationProps):
    """Type encapsulating layer properties."""

    id: StrictStr
    """Unique identifier of the layer."""

    type: Optional[LayerType]
    """Type of the layer."""

    data_id: StrictStr
    """Unique identifier of the dataset this layer visualizes."""

    fields: Dict[StrictStr, Optional[StrictStr]]
    """Dictionary that maps fields that the layer requires for visualization to appropriate dataset fields."""

    label: StrictStr
    """Canonical label of this layer."""

    is_visible: StrictBool
    """Flag indicating whether layer is visible or not."""

    config: LayerConfig
    """Layer configuration specific to its type."""


class _LayerGroupUpdateProps(CamelCaseBaseModel):

    label: Optional[StrictStr]
    """Canonical label of this layer group."""

    is_visible: Optional[StrictBool]
    """Flag indicating whether layer group is visible or not."""

    layers: Optional[List[StrictStr]]
    """An array of new layer properties, or existing layer identifier to update the group with."""


class _LayerGroupCreationProps(_LayerGroupUpdateProps):

    id: Optional[StrictStr]
    """Unique identifier of the layer group."""

    label: Optional[StrictStr]
    """Canonical label of this layer group."""

    is_visible: Optional[StrictBool]
    """Flag indicating whether layer group is visible or not."""

    layers: Optional[List[StrictStr]]
    """An array of new layer properties, or existing layer identifier to update the group with."""


class LayerGroup:
    """A conceptual group used to organize layers."""

    id: StrictStr
    """Unique identifier of the layer group."""

    label: StrictStr
    """Canonical label of this layer group."""

    is_visible: StrictBool
    """Flag indicating whether layer group is visible or not."""

    layers: List[StrictStr]
    """Layers that are part of this group, sorted in the order in which they are shown."""


class _LayerTimelineUpdateProps(CamelCaseBaseModel):

    current_time: Optional[Number]
    """Current time on the timeline in milliseconds."""

    is_animating: Optional[StrictBool]
    """Flag indicating whether the timeline is animating or not."""

    is_visible: Optional[StrictBool]
    """Flag indicating whether the timeline is visible or not."""

    animation_speed: Optional[Number]
    """Speed at which timeline is animating."""

    time_format: Optional[StrictStr]
    """Time format that the timeline is using in day.js supported format.

    https://day.js.org/docs/en/display/format
    """

    timezone: Optional[StrictStr]
    """Timezone that the timeline is using in tz format.

    https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
    """


class LayerTimeline(_LayerTimelineUpdateProps):

    current_time: Number
    """Current time on the timeline in milliseconds."""

    domain: TimeRange
    """Range of time that the timeline shows."""

    is_animating: StrictBool
    """Flag indicating whether the timeline is animating or not."""

    is_visible: StrictBool
    """Flag indicating whether the timeline is visible or not."""

    animation_speed: Number
    """Speed at which timeline is animating."""

    time_format: StrictStr
    """Time format that the timeline is using in day.js supported format.

    https://day.js.org/docs/en/display/format
    """

    timezone: Optional[StrictStr]
    """Timezone that the timeline is using in tz format.

    https://en.wikipedia.org/wiki/List_of_tz_database_time_zones
    """

    time_steps: Optional[List[Number]]
    """Step duration for all the animation keyframes in milliseconds."""


class LayerEventHandlers(CamelCaseBaseModel):
    on_layer_timeline_update: Optional[Callable[[LayerTimeline], None]]


###########
# ACTIONS #
###########


class GetLayersAction(Action):
    type: ActionType = ActionType.GET_LAYERS


class GetLayerByIdAction(Action):
    class Meta(Action.Meta):
        args = ["layer_id"]

    type: ActionType = ActionType.GET_LAYER_BY_ID
    layer_id: StrictStr


class AddLayerAction(Action):
    class Meta(Action.Meta):
        args = ["layer"]

    type: ActionType = ActionType.ADD_LAYER
    layer: _LayerCreationProps


class UpdateLayerAction(Action):
    class Meta(Action.Meta):
        args = ["layer_id", "values"]

    type: ActionType = ActionType.UPDATE_LAYER
    layer_id: StrictStr
    values: _LayerUpdateProps


class RemoveLayerAction(Action):
    class Meta(Action.Meta):
        args = ["layer_id"]

    type: ActionType = ActionType.REMOVE_LAYER
    layer_id: StrictStr


class GetLayerGroupsAction(Action):

    type: ActionType = ActionType.GET_LAYER_GROUPS


class GetLayerGroupByIdAction(Action):
    class Meta(Action.Meta):
        args = ["layer_group_id"]

    type: ActionType = ActionType.GET_LAYER_GROUP_BY_ID
    layer_group_id: StrictStr


class AddLayerGroupAction(Action):
    class Meta(Action.Meta):
        args = ["layer_group"]

    type: ActionType = ActionType.ADD_LAYER_GROUP
    layer_group: _LayerGroupCreationProps


class UpdateLayerGroupAction(Action):
    class Meta(Action.Meta):
        args = ["layer_group_id", "values"]

    type: ActionType = ActionType.UPDATE_LAYER_GROUP
    layer_group_id: StrictStr
    values: _LayerGroupUpdateProps


class RemoveLayerGroupAction(Action):
    class Meta(Action.Meta):
        args = ["layer_group_id"]

    type: ActionType = ActionType.REMOVE_LAYER_GROUP
    layer_group_id: StrictStr


class GetLayerTimelineAction(Action):
    type: ActionType = ActionType.GET_LAYER_TIMELINE


class UpdateLayerTimelineAction(Action):
    class Meta(Action.Meta):
        args = ["values"]

    type: ActionType = ActionType.UPDATE_LAYER_TIMELINE
    values: _LayerTimelineUpdateProps


###########
# METHODS #
###########


class BaseLayerApiMethods:
    @abstractmethod
    def add_layer(
        self, layer: Union[_LayerCreationProps, dict, None] = None, **kwargs: Any
    ) -> Optional[Layer]:
        ...

    @abstractmethod
    def add_layer_group(
        self,
        layer_group: Union[_LayerGroupCreationProps, dict, None] = None,
        **kwargs: Any
    ) -> Optional[LayerGroup]:
        ...


class BaseInteractiveLayerApiMethods:
    @abstractmethod
    def get_layers(self) -> List[Layer]:
        ...

    @abstractmethod
    def get_layer_by_id(self, layer_id: str) -> Optional[Layer]:
        ...

    @abstractmethod
    def update_layer(
        self, layer_id: str, values: Union[_LayerUpdateProps, dict, None], **kwargs: Any
    ) -> Layer:
        ...

    @abstractmethod
    def remove_layer(self, layer_id: str) -> None:
        ...

    @abstractmethod
    def get_layer_groups(self) -> List[LayerGroup]:
        ...

    @abstractmethod
    def get_layer_group_by_id(self, layer_group_id: str) -> Optional[LayerGroup]:
        ...

    @abstractmethod
    def update_layer_group(
        self,
        layer_group_id: str,
        values: Union[_LayerGroupUpdateProps, dict, None],
        **kwargs: Any
    ) -> LayerGroup:
        ...

    @abstractmethod
    def remove_layer_group(self, layer_group_id: str) -> None:
        ...

    @abstractmethod
    def get_layer_timeline(self) -> Optional[LayerTimeline]:
        ...

    @abstractmethod
    def update_layer_timeline(self, values) -> LayerTimeline:
        ...


class LayerApiNonInteractiveMixin(BaseLayerApiMethods):
    """Layer methods that are supported in non-interactive (i.e. pure HTML) maps"""

    transport: BaseNonInteractiveTransport

    @validate_kwargs(positional_only=["layer"])
    def add_layer(
        self, layer: Union[_LayerCreationProps, dict, None] = None, **kwargs: Any
    ) -> None:
        """Adds a new layer to the map.

        Args:
            layer (Union[LayerCreationProps, dict, None], optional): The layer to add. Defaults to None.
        """
        action = AddLayerAction(layer=layer if layer is not None else kwargs)
        self.transport.send_action(action=action)

    @validate_kwargs(positional_only=["layer_group"])
    def add_layer_group(
        self,
        layer_group: Union[_LayerGroupCreationProps, dict, None] = None,
        **kwargs: Any
    ) -> None:
        """Adds a new layer group to the map.

        Args:
            layer_group (Union[_LayerGroupCreationProps, dict, None], optional): The layer group to add. Defaults to None.
        """
        action = AddLayerGroupAction(
            layer_group=layer_group if layer_group is not None else kwargs
        )
        self.transport.send_action(action=action)


class LayerApiInteractiveMixin(BaseLayerApiMethods, BaseInteractiveLayerApiMethods):
    """Layer methods that are supported in interactive (i.e. widget) maps"""

    transport: BaseInteractiveTransport

    @validate_kwargs(positional_only=["layer"])
    def add_layer(
        self, layer: Union[_LayerCreationProps, dict, None] = None, **kwargs: Any
    ) -> Layer:
        """Adds a new layer to the map.

        Args:
            layer (Union[LayerCreationProps, dict, None], optional): The layer to add. Defaults to None.

        Returns:
            Layer: The layer that was added.
        """
        action = AddLayerAction(layer=layer if layer is not None else kwargs)
        return self.transport.send_action_non_null(action=action, response_class=Layer)

    def get_layers(self) -> List[Layer]:
        """Gets all the layers currently available in the map.

        Returns:
            List[Layer]: An array of layers.
        """
        action = GetLayersAction()
        return self.transport.send_action_non_null(
            action=action, response_class=List[Layer]
        )

    @validate_kwargs(positional_only=["layer_id"])
    def get_layer_by_id(self, layer_id: str) -> Optional[Layer]:
        """Retrieves a layer by its identifier if it exists.

        Args:
            layer_id (str): Identifier of the layer to get.

        Returns:
            Optional[Layer]: Layer with a given identifier, or null if one doesn't exist.
        """
        action = GetLayerByIdAction(layer_id=layer_id)
        return self.transport.send_action(action=action, response_class=Layer)

    @validate_kwargs(positional_only=["layer_id", "values"])
    def update_layer(
        self, layer_id: str, values: Union[_LayerUpdateProps, dict, None], **kwargs: Any
    ) -> Layer:
        """Updates an existing layer with given values.

        Args:
            layer_id (str): The id of the layer to update.
            values (Union[LayerUpdateProps, dict, None]): The values to update.

        Returns:
            Layer: The updated layer.
        """
        action = UpdateLayerAction(
            layer_id=layer_id, values=values if values is not None else kwargs
        )
        return self.transport.send_action_non_null(action=action, response_class=Layer)

    @validate_kwargs(positional_only=["layer_id"])
    def remove_layer(self, layer_id: str) -> None:
        """Removes a layer from the map.

        Args:
            layer_id (str): The id of the layer to remove
        """
        action = RemoveLayerAction(layer_id=layer_id)
        self.transport.send_action(action=action, response_class=None)

    @validate_kwargs(positional_only=["layer_group"])
    def add_layer_group(
        self,
        layer_group: Union[_LayerGroupCreationProps, dict, None] = None,
        **kwargs: Any
    ) -> LayerGroup:
        """Adds a new layer group to the map.

        Args:
            layer_group (Union[_LayerGroupCreationProps, dict, None], optional): The layer group to add. Defaults to None.

        Returns:
            LayerGroup: The layer group that was added.
        """
        action = AddLayerGroupAction(
            layer_group=layer_group if layer_group is not None else kwargs
        )
        return self.transport.send_action_non_null(
            action=action, response_class=LayerGroup
        )

    def get_layer_groups(self) -> List[LayerGroup]:
        """Gets all the layer groups currently available in the map.

        Returns:
            List[LayerGroup]: An array of layer groups.
        """
        action = GetLayerGroupsAction()
        return self.transport.send_action_non_null(
            action=action, response_class=List[LayerGroup]
        )

    @validate_kwargs(positional_only=["layer_group_id"])
    def get_layer_group_by_id(self, layer_group_id: str) -> Optional[LayerGroup]:
        """Retrieves a layer group by its identifier if it exists.

        Args:
            layer_group_id (str): Identifier of the layer group to get.

        Returns:
            Optional[LayerGroup]: Layer group with a given identifier, or null if one doesn't exist.
        """
        action = GetLayerGroupByIdAction(layer_group_id=layer_group_id)
        return self.transport.send_action(action=action, response_class=LayerGroup)

    @validate_kwargs(positional_only=["layer_group_id", "values"])
    def update_layer_group(
        self,
        layer_group_id: str,
        values: Union[_LayerGroupUpdateProps, dict, None],
        **kwargs: Any
    ) -> LayerGroup:
        """Updates an existing layer group with given values.

        Args:
            layer_group_id (str): The id of the layer group to update.
            values (Union[_LayerGroupUpdateProps, dict, None]): The values to update.

        Returns:
            LayerGroup: The updated layer group.
        """
        action = UpdateLayerGroupAction(
            layer_group_id=layer_group_id,
            values=values if values is not None else kwargs,
        )
        return self.transport.send_action_non_null(
            action=action, response_class=LayerGroup
        )

    @validate_kwargs(positional_only=["layer_group_id"])
    def remove_layer_group(self, layer_group_id: str) -> None:
        """Removes a layer group from the map.

        Args:
            layer_group_id (str): The id of the layer group to remove
        """
        action = RemoveLayerGroupAction(layer_group_id=layer_group_id)
        self.transport.send_action(action=action, response_class=None)

    def get_layer_timeline(self) -> Optional[LayerTimeline]:
        """Gets the current layer timeline configuration.

        Returns:
            Optional[LayerTimeline]: The layer timeline configuration.
        """
        action = GetLayerTimelineAction()
        return self.transport.send_action(action=action, response_class=LayerTimeline)

    @validate_kwargs(positional_only=["values"])
    def update_layer_timeline(
        self, values: Union[_LayerTimelineUpdateProps, dict, None] = None, **kwargs: Any
    ) -> LayerTimeline:
        """Updates the current layer timeline configuration.

        Args:
            values (Union[LayerTimelineUpdateProps, dict, None], optional): The new layer timeline values. Defaults to None.

        Returns:
            LayerTimeline: The updated layer timeline.
        """
        action = UpdateLayerTimelineAction(
            values=values if values is not None else kwargs
        )
        return self.transport.send_action_non_null(
            action=action, response_class=LayerTimeline
        )
