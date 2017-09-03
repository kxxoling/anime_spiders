<template lang="jade">
.anime-list
  .list-container
    anime.anime(v-for="anime in animes", :anime="anime", key="anime.id")

  md-pagination.pagination(
    :current-page="currentPage",
    :pages-count="pagesCount",
    :currentChange="changeCurrent"
  )

</template>

<script>
import { mapGetters, mapActions } from 'vuex';
import Anime from '@/components/Anime';
import MdPagination from '@/components/MdPagination';

const PAGE_SIZE = 30;

export default {
  data() {
    return {
      currentPage: 1,
    };
  },
  mounted() {
    if (!this.animes.length && !this.isFetching) {
      this.getAnimes({ page: 1, size: PAGE_SIZE });
    }
  },
  computed: {
    ...mapGetters({
      animes: 'animes',
      isFetching: 'isFetchingAnimes',
      pagesCount: 'animePagesCount',
    }),
  },
  methods: {
    ...mapActions({
      getAnimes: 'getAnimes',
    }),
    fetchPage(val) {
      this.getAnimes({ page: val, size: PAGE_SIZE });
    },
    changeCurrent(val) {
      this.currentPage = val;
      this.fetchPage(val);
    },
  },
  components: {
    Anime, MdPagination,
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
