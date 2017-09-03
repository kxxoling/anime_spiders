<template lang="jade">
.nav
  md-toolbar.md-fixed
    md-button.md-icon-button(@click='toggleLeftSidenav')
      md-icon menu
    h2.md-title Anime Spiders FE
  md-sidenav.md-fixed.md-left(
    ref='leftSidenav',
    @open="open('Left')",
    @close="close('Left')"
  )
    md-toolbar.md-large
      .md-toolbar-container
        h2.md-title Navigation
    md-list
      md-list-item
        router-link(to="/cg")
          i.fa.fa-picture-o
          | CG
      md-list-item
        router-link(to="/anime")
          i.fa.fa-imdb
          | Anime
      md-list-item
        router-link(exact to="/torrent")
          i.fa.fa-download
          | Torrent
      md-list-item
        router-link(exact to="/shortvideo")
          i.fa.fa-video-camera
          | Short Video
</template>

<script>
export default {

  methods: {
    toggleLeftSidenav() {
      this.$refs.leftSidenav.toggle();
    },
    open() {},
    close() {},
  },
};
</script>

<style lang="stylus" scoped>
i.fa
  margin-right 0.5rem

.el-menu-item
  padding 0 2rem

.float-right
  float right

  a
    text-decoration none
</style>
