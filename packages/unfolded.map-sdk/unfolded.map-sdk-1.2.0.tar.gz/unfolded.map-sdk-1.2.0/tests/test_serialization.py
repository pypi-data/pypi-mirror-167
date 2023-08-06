import importlib
import inspect
import logging

import pytest
from pydantic import parse_obj_as

from unfolded.map_sdk.api.dataset_api import (
    Dataset,
    LocalDataset,
    RasterTileDataset,
    RasterTileLocalItemMetadata,
    VectorTileDataset,
    VectorTileLocalMetadata,
)
from unfolded.map_sdk.utils.serialization import serialize_action

from .fixtures import SERIALIZED_ACTIONS
from .fixtures.dataset_api import (
    LOCAL_RESPONSE,
    RASTER_TILE_RESPONSE,
    VECTOR_TILE_RESPONSE,
)


class TestActionSerialization:
    def test_ensure_all_actions_tested(self):
        """All Actions should be listed in SERIALIZED_ACTIONS"""

        MAP_API = importlib.import_module("unfolded.map_sdk.api.map_api")
        DATASET_API = importlib.import_module("unfolded.map_sdk.api.dataset_api")
        LAYER_API = importlib.import_module("unfolded.map_sdk.api.layer_api")
        FILTER_API = importlib.import_module("unfolded.map_sdk.api.filter_api")
        API_MODULES = [MAP_API, DATASET_API, LAYER_API, FILTER_API]

        all_actions = set()

        for api_module in API_MODULES:
            for name, obj in inspect.getmembers(api_module, inspect.isclass):
                if name.endswith("Action") and inspect.getmodule(obj) in API_MODULES:
                    all_actions.add(obj)

        listed_actions = set()
        for (action, _) in SERIALIZED_ACTIONS:
            listed_actions.add(action.__class__)

        diff_actions = all_actions.symmetric_difference(listed_actions)
        assert not diff_actions, f"Actions listed but not tested: {diff_actions}"

    @pytest.mark.parametrize("action,serialized", SERIALIZED_ACTIONS)
    def test_serialize_action(self, action, serialized, caplog):
        """All fields other than `type` and `messageId` should be included within the `data` key."""
        with caplog.at_level(logging.DEBUG):
            d, _ = serialize_action(action)

        # make sure there are no debug warnings in message serialization
        assert not caplog.text, f"Action not serialized properly: {caplog.text}"

        # messageId is a unique uuid and won't match
        d.pop("messageId")
        serialized.pop("messageId")

        assert (
            d == serialized
        ), f"Message not serialized as expected: {d} vs {serialized}"


class TestDataset:
    """Tests relating to dataset serialization/deserialization"""

    def test_deserialize(self):

        local_dataset = parse_obj_as(Dataset, LOCAL_RESPONSE)
        assert isinstance(local_dataset, LocalDataset)

        vector_tile_dataset = parse_obj_as(Dataset, VECTOR_TILE_RESPONSE)
        assert isinstance(vector_tile_dataset, VectorTileDataset)
        assert isinstance(vector_tile_dataset.metadata, VectorTileLocalMetadata)

        raster_tile_dataset = parse_obj_as(Dataset, RASTER_TILE_RESPONSE)
        assert isinstance(raster_tile_dataset, RasterTileDataset)
        assert isinstance(raster_tile_dataset.metadata, RasterTileLocalItemMetadata)
