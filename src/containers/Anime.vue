<template lang="jade">
.anime-list
  anime(v-for="anime in animes", :anime="anime")
</template>

<script>
import Anime from '@/components/Anime';

export default {
  data() {
    return {
      animes: [{
        id: 117,
        crawled_from: 'bangumi.tv',
        site_pk: 118335,
        link: '/subject/118335',
        cover: '//lain.bgm.tv/pic/cover/c/22/ed/118335_tjSh3.jpg',
        name: '进击的巨人 第二季',
        orig_name: '進撃の巨人 Season 2',
        pub_date: '12话 /  2017年4月1日 / 諫山創（別冊少年マガジン連載／講談社）',
      }],
    };
  },
  components: {
    Anime,
  },
};
</script>

<style lang="stylus" scoped>

</style>
