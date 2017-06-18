<template lang="jade">
.short-video(@click="play=!play")
  figure.preview
    img(v-bind:src="preview")
    .play-button.fa.fa-play-circle(v-if="!play && video.file_ext==='mp4'")

  video.short-view-play(
    v-if="video.file_ext==='mp4' && play",
    poster="preview",
    autoplay
  )
    source(v-bind:src="source", type="video/mp4")

</template>

<script>
export default {
  props: {
    video: Object,
  },
  data() {
    return {
      play: false,
    };
  },
  computed: {
    preview() {
      return `/storage/sakuga/${this.video.md5}.jpg`;
    },
    source() {
      return `/storage/sakuga/${this.video.md5}.${this.video.file_ext}`;
    },
  },
};
</script>

<style lang="stylus" scoped>
.short-video
  display flex
  height 15rem
  width 20rem
  cursor pointer
  overflow hidden

  .preview
    width 100%
    height 100%
    margin 0
    display flex
    align-items center
    justify-content center

    img
      width 100%
      height auto

    .play-button
      color white
      position absolute
      background-color rgba(0, 0, 0, 0.3)
      width 4rem
      font-size 4rem
      text-align center
      border-radius 2rem

  .short-view-play
    width 100%
    // height 100%
</style>
