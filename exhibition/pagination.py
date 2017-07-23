from rest_framework.pagination import PageNumberPagination


class PagesCountPagination(PageNumberPagination):
    page_size_query_param = 'size'
    page_query_param = 'page'
