<template lang="jade">
.torrent-list
  .list-container
    torrent.torrent(v-for="torrent in torrents", :torrent="torrent", key="torrent.id")
  el-pagination.pagination(
    layout="prev, pager, next",
    :page-count="pagesCount",
    @current-change="fetchPage"
  )
</template>

<script>
import { mapGetters, mapActions } from 'vuex';
import Torrent from '@/components/Torrent';

const PAGE_SIZE = 30;

export default {
  data() {
    return {
    };
  },
  mounted() {
    if (!this.torrents.length) {
      this.getTorrents({ page: 1, size: PAGE_SIZE });
    }
  },
  computed: {
    ...mapGetters({
      torrents: 'torrents',
      isFetching: 'isFetchingTorrents',
      pagesCount: 'videoPagesCount',
    }),
  },
  methods: {
    ...mapActions({
      getTorrents: 'getTorrents',
    }),
    fetchPage(val) {
      this.getTorrents({ page: val, size: PAGE_SIZE });
    },
  },
  components: {
    Torrent,
  },
  metaInfo: {
    title: 'Torrents',
  },
};
</script>

<style lang="stylus" scoped>
.torrent-list
  .torrent
    margin-bottom 1rem
</style>
