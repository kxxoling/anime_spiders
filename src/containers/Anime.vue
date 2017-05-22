<template lang="jade">
.anime-list
  anime.anime(v-for="anime in animes", :anime="anime", key="anime.id")
</template>

<script>
import { mapGetters, mapActions } from 'vuex';
import Anime from '@/components/Anime';

export default {
  data() {
    return {
    };
  },
  mounted() {
    if (!this.animes.length) {
      this.getAnimes({ page: 1, size: 10 });
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
  },
  components: {
    Anime,
  },
};
</script>

<style lang="stylus" scoped>
.anime-list
  margin 1rem
  display flex
  flex-flow row wrap
  justify-content space-between

  .anime
    margin-botom 2rem
</style>
