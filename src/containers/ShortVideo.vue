<template lang="jade">
.video-list
  short-video.video(v-for="video in shortVideos", :video="video", key="video.id")
</template>

<script>
import { mapGetters, mapActions } from 'vuex';
import ShortVideo from '@/components/ShortVideo';

export default {
  data() {
    return {
    };
  },
  mounted() {
    if (!this.shortVideos.length) {
      this.getVideos({ page: 1, size: 10 });
    }
  },
  computed: {
    ...mapGetters({
      shortVideos: 'shortVideos',
      isFetching: 'isFetching',
    }),
  },
  methods: {
    ...mapActions({
      getVideos: 'getVideos',
    }),
  },
  components: {
    ShortVideo,
  },
  metaInfo: {
    title: 'Short Videos',
  },
};
</script>

<style lang="stylus" scoped>
.video-list
  margin 1rem
  display flex
  flex-flow row wrap
  justify-content space-between

  .video
    margin-bottom 1rem
</style>
