import base64

from pyinjective.client.model.pagination import PaginationOption


class TestPaginationOption:
    def test_create_pagination_request(self):
        next_page_key = b"next page key"
        encoded_next_page_key = base64.b64encode(next_page_key).decode()
        pagination_option = PaginationOption(
            encoded_page_key=encoded_next_page_key,
            skip=5,
            limit=10,
            start_time=3,
            end_time=4,
            reverse=False,
            count_total=True,
            from_number=105,
            to_number=135,
        )

        page_request = pagination_option.create_pagination_request()
        assert page_request.key == next_page_key
        assert page_request.offset == pagination_option.skip
        assert page_request.limit == pagination_option.limit
        assert not page_request.reverse
        assert page_request.count_total

    def test_next_key_is_none_for_empty_encoded_page_key(self):
        pagination_option = PaginationOption(
            encoded_page_key="",
        )
        page_request = pagination_option.create_pagination_request()

        assert page_request.key == b""
