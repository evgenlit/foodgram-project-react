from rest_framework.pagination import PageNumberPagination


class SubscribeUserPagination(PageNumberPagination):
    page_size_query_param = 'limit'
