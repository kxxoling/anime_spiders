<template lang="jade">
.anime-list
  .list-container
    anime.anime(v-for="anime in animes", :anime="anime", key="anime.id")
  el-pagination.pagination(
    layout="prev, pager, next",
    :total="100",
    @current-change="fetchPage"
  )
</template>

<script>
import { mapGetters, mapActions } from 'vuex';
import Anime from '@/components/Anime';

const PAGE_SIZE = 30;

export default {
  data() {
    return {
    };
  },
  mounted() {
    if (!this.animes.length) {
      this.getAnimes({ page: 1, size: PAGE_SIZE });
    }
  },
  computed: {
    ...mapGetters({
      animes: 'animes',
      isFetching: 'isFetching',
    }),
  },
  methods: {
    ...mapActions({
      getAnimes: 'getAnimes',
    }),
    fetchPage(val) {
      this.getAnimes({ page: val, size: PAGE_SIZE });
    },
  },
  components: {
    Anime,
  },
  metaInfo: {
    title: 'Animes',
  },
};
</script>

<style lang="stylus" scoped>
.pagination
  text-align center
  margin-bottom 2rem

.list-container
  .anime
    margin-bottom 2rem
</style>
