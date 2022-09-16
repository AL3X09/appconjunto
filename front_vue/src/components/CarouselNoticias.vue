<template>

  <li v-for="item in anoticias">
    <Carousel :autoplay="2000"  :itemsToShow="4.0" :wrapAround="true">
      <Slide v-for="sliden in item.data" :key="sliden">
        <div class="carousel__item">

          <b-card no-body class="overflow-hidden">
                <b-card-img :src="sliden.imagen" alt="Image" class="rounded-0"></b-card-img>
                <b-card-body>
                  <b-card-title>{{ sliden.titulo }}</b-card-title>
                  <b-card-sub-title class="mb-2">{{ sliden.subtitulo }}</b-card-sub-title>
                  <b-card-text>
                    {{ sliden.cuerpo }}
                  </b-card-text>
                </b-card-body>
                <b-button href="#" variant="primary">Seguir Leyendo</b-button>
          </b-card>

        </div>
      </Slide>

      <template #addons>
        <Pagination />
      </template>
    </Carousel>
  </li>
 
</template>

<script>
import { defineComponent } from 'vue'
import { Carousel, Pagination, Slide } from 'vue3-carousel';
import http from "../http-common";

import 'vue3-carousel/dist/carousel.css';

export default {
  data() {
      return {
        anoticias: [],
      }
    },
    mounted() {
      this.getDataN();
    },
    methods: {
      fortmatResponse(res) {
        return JSON.stringify(res, null, 2);
      },
      async getDataN() {
        try {
        const res = await http.get("noticia/api/listar/");
        const result = {
          data: res.data,
        };
        this.anoticias.push(result);
      } catch (err) {
        this.anoticias.push(this.fortmatResponse(err.response?.data) || err);
      }
      },
      clearGetOutput() {
        this.getDataN = null;
      },
    },
    components: {
      Carousel,
      Slide,
      Pagination,
    },
};
</script>

<style scoped>

.carousel__slide > .carousel__item {
  transform: scale(1);
  opacity: 0.5;
  transition: 0.5s;
}
.carousel__slide--visible > .carousel__item {
  opacity: 1;
  transform: rotateY(0);
}
.carousel__slide--next > .carousel__item {
  /*transform: scale(0.9) translate(-10px);*/
  transform: scale(0.9) translate(-5px);
}
.carousel__slide--prev > .carousel__item {
  transform: scale(0.9) translate(5px);
}
.carousel__slide--active > .carousel__item {
  transform: scale(1.1);
}

li {
    list-style-type: none;
}

</style>