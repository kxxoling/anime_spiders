<template lang="jade">
.cg-list()
  .cg(v-for="cg in cgs", key="cg.id", @click="showCg(cg)")
    cg(:cg="cg")
  el-dialog(title="", :visible.sync="showDetails", size="large")
    .detailed(v-if="checked")
      figure.figure
        img(v-bind:src="`/storage/danbooru_donmai_us/${checked.large_file_url.split('/').pop()}`")
      .info
        .copyright-tags(v-if="checked.copyright_tags")
          label 作品：
          .tag(v-for="tag in checked.copyright_tags")
        .character-tags(v-if="checked.character_tags")
          label 人物：
          .tag(v-for="tag in checked.character_tags")
        .general-tags(v-if="checked.general_tags")
          label 一般 tag：
          .tag(v-for="tag in checked.general_tags")
        .artist-tags(v-if="checked.artist_tags")
          label 作者：
          .tag(v-for="tag in checked.artist_tags")
        .source
          label 来源：
          a(href="checked.source") {{ checked.source }}
        .rating
          label 分级：
          span {{ checked.rating }}
        .score
          label 评分：
          span {{ checked.score }}
        .crawled_from
          a(v-bind:href="'//danbooru.donmai.us/posts/' + checked.site_pk", target="_blank") danbooru.donmai.us
        .pixiv(v-if="checked.pixiv_id")
          label Pixiv ID：
          a(v-bind:href="'//www.pixiv.net/member_illust.php?mode=medium&illust_id=' + checked.pixiv_id") {{ checked.pixiv_id }}
</template>

<script>
import { mapGetters, mapActions } from 'vuex';
import Cg from '@/components/Cg';

export default {
  data() {
    return {
      showDetails: false,
      checked: null,
    };
  },
  mounted() {
    if (!this.cgs.length) {
      this.getCgs({ page: 1, size: 10 });
    }
  },
  computed: {
    ...mapGetters({
      cgs: 'cgs',
      isFetching: 'isFetching',
    }),
  },
  methods: {
    ...mapActions({
      getCgs: 'getCgs',
    }),
    showCg(cg) {
      this.showDetails = true;
      this.checked = cg;
    },
  },
  components: {
    Cg,
  },
  metaInfo: {
    title: 'Gallery',
  },
};
</script>

<style lang="stylus" scoped>
.cg-list
  margin 1rem auto
  display flex
  flex-flow row wrap
  justify-content space-between
  width 1000px
  *
    word-break break-all

  .cg
    margin-bottom 2rem
    cursor pointer
.detailed
  font-size 1.2rem
  line-height 2rem
  display flex
  height 100%
  position relative

  .figure
    flex 1
    max-height 100%
    max-width 40%

    img
      max-height 100%
      max-width 100%

  .info
    flex 1
    width 50rem
    max-width 60%
    padding-left 1rem
    padding-right 1rem
</style>
