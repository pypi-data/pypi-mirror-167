from pytest_mock import MockerFixture

from unfolded.map_sdk.map.widget import SyncWidgetMap


class TestAddDataset:
    def test_raster_custom_stac_item(
        self, mocker: MockerFixture, sentinel2_stac_item: dict
    ):
        mocked_send_widget_message = mocker.patch(
            "unfolded.map_sdk.transport.widget.BlockingWidgetTransport._send_widget_message"
        )
        _ = mocker.patch(
            "unfolded.map_sdk.transport.widget.BlockingWidgetTransport._wait_for_future"
        )

        unfolded_map = SyncWidgetMap()

        raster_tile_dataset = {"type": "raster-tile", "metadata": sentinel2_stac_item}
        unfolded_map.add_dataset(raster_tile_dataset)

        # TODO: assert that the right object was sent to JS using call_args_list
        print(mocked_send_widget_message.call_args_list)

    def test_raster_custom_stac_collection(
        self, mocker: MockerFixture, sentinel2_stac_collection: dict
    ):
        mocked_send_widget_message = mocker.patch(
            "unfolded.map_sdk.transport.widget.BlockingWidgetTransport._send_widget_message"
        )
        _ = mocker.patch(
            "unfolded.map_sdk.transport.widget.BlockingWidgetTransport._wait_for_future"
        )

        unfolded_map = SyncWidgetMap()

        raster_tile_dataset = {
            "type": "raster-tile",
            "metadata": sentinel2_stac_collection,
        }
        unfolded_map.add_dataset(raster_tile_dataset)

        # TODO: assert that the right object was sent to JS using call_args_list
        print(mocked_send_widget_message.call_args_list)
