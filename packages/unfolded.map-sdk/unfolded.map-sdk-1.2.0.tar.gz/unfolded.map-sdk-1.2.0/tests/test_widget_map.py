from unfolded.map_sdk.map.widget import SyncWidgetMap


class TestTransport:
    def test_event_handler_merge(self):

        m = SyncWidgetMap()
        transport = m.transport

        func1 = lambda view: print(1)
        func2 = lambda mouse_event: print(2)
        func3 = lambda view: print(3)
        func4 = lambda filter: print(4)

        event_handlers_1 = {"on_view_update": func1, "on_click": func2}

        transport.set_event_handlers(event_handlers_1)
        assert transport.event_handlers == event_handlers_1

        event_handlers_2 = {"on_view_update": func3, "on_filter_update": func4}

        transport.set_event_handlers(event_handlers_2)

        event_handlers_final = {
            "on_view_update": func3,
            "on_click": func2,
            "on_filter_update": func4,
        }
        assert transport.event_handlers == event_handlers_final
