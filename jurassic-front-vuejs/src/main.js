import * as Vue from 'vue';
// Official documentation -> https://router.vuejs.org/guide/#html
import * as  VueRouter from 'vue-router';

// Import defined Views
import App from "@/App";


import HomeView from "@/views/HomeView";
import NotFound from "@/views/NotFound";

import DinoTrexView from "@/views/DinoTrexView";
import DinoRaptorView from "@/views/DinoRaptorView";
import DinoMosasaurioView from "@/views/DinoMosasaurioView";
import DinoArgSaurioView from "@/views/DinoArgSaurioView";

import HelpAddDinoView from "@/views/HelpAddDinoView";
import HelpAttackDinoView from "@/views/HelpAttackDinoView";

// Here we will define all the routes
const routes = [
    {path: '/', name: "HomeRoute", component: HomeView},

    {path: '/dino/trex',        name: "DinoTrexRoute", component: DinoTrexView},
    {path: '/dino/raptor',      name: "DinoRaptorRoute", component: DinoRaptorView},
    {path: '/dino/mosa',        name: "DinoMosasaurioRoute", component: DinoMosasaurioView},
    {path: '/dino/argsaurio',   name: "DinoArgSaurioRoute", component: DinoArgSaurioView},
    
    {path: '/help/dino/add',    name: "HelpAddDinoRoute", component: HelpAddDinoView},
    {path: '/help/dino/attack', name: "HelpAttackDinoRoute", component: HelpAttackDinoView},
    
    {path: '/:pathMatch(.*)*', component: NotFound}
];

// Create the object router, add pass the routes above
const router = VueRouter.createRouter({
    history: VueRouter.createWebHashHistory(),
    routes,
});

// Add router to the Vue instance
const app = Vue.createApp(App);
app.use(router);
app.mount('#app');