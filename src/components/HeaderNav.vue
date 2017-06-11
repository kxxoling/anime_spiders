<template lang="jade">
el-menu(theme="dark", mode="horizontal", router="true")
  el-menu-item(index="/cg")
    i.fa.fa-picture-o
    | CG
  el-menu-item(index="/anime")
    i.fa.fa-imdb
    | Anime
  el-menu-item(index="/shortvideo")
    i.fa.fa-video-camera
    | Short Video
  el-menu-item(index="/torrent")
    i.fa.fa-download
    | Torrent
</template>

<style lang="stylus" scoped>
i.fa
  margin-right 0.5rem
</style>
