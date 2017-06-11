<template lang="jade">
.torrent
  h2.title {{ torrent.title }}
  div
    label 类型：
    span {{ torrent.category }}
  div
    label 来源：
    span {{ torrent.crawled_from }}
  div
    label 下载：
    span(v-if="torrent.magnet")
      a(v-bind:href="torrent.magnet")
        i.fa.fa-magnet
    span(v-if="torrent.torrent_path")
      a(v-bind:href="torrent.torrent_path")
        i.fa.fa-download
</template>

<script>
export default {
  props: {
    torrent: Object,
  },
  data() {
    return {};
  },
  computed: {
  },
};
</script>

<style lang="stylus" scoped>
.torrent
  height 12rem
  width 20rem
  padding 1rem
  background green

  h2
    font-size 1.1rem

  div
    line-height 1.2rem
    height 1.2rem
</style>
