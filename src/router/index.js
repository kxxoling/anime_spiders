import Vue from 'vue';
import Router from 'vue-router';
import Index from '@/containers/Index';
import Cg from '@/containers/Cg';
import Anime from '@/containers/Anime';
import ShortVideo from '@/containers/ShortVideo';
import Torrent from '@/containers/Torrent';

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Index',
      component: Index,
    },
    {
      path: '/cg',
      name: 'CG',
      component: Cg,
    },
    {
      path: '/anime',
      name: 'Anime',
      component: Anime,
    },
    {
      path: '/shortvideo',
      name: 'Shot Videos',
      component: ShortVideo,
    },
    {
      path: '/torrent',
      name: 'Torrent',
      component: Torrent,
    },
  ],
});
