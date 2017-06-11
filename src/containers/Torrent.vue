<template lang="jade">
.torrent-list
  torrent.torrent(v-for="torrent in torrents", :torrent="torrent", key="torrent.id")
</template>

<script>
import { mapGetters, mapActions } from 'vuex';
import Torrent from '@/components/Torrent';

export default {
  data() {
    return {
    };
  },
  mounted() {
    if (!this.torrents.length) {
      this.getTorrents({ page: 1, size: 10 });
    }
  },
  computed: {
    ...mapGetters({
      torrents: 'torrents',
      isFetching: 'isFetching',
    }),
  },
  methods: {
    ...mapActions({
      getTorrents: 'getTorrents',
    }),
  },
  components: {
    Torrent,
  },
};
</script>

<style lang="stylus" scoped>
.torrent-list
  margin 1rem
  display flex
  flex-flow row wrap
  justify-content space-between

  .torrent
    margin-bottom 1rem
</style>
