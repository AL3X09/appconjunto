
<template>

  <div v-if="vgetHead">
    <div v-for="resulth in vgetHead" :key="resulth.data.id">
        <!-- Navigation-->
        <nav class="navbar navbar-expand-lg bg-light">
          <div class="container-fluid">
            <img :src="resulth.data.logo" width="25" height="25"/>
            <RouterLink to="/" class="navbar-brand">{{resulth.data.name}}</RouterLink>
            <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
              <i class="bi bi-list"></i>
            </button>
            <div class="collapse navbar-collapse" id="navbarSupportedContent">
              <ul class="navbar-nav flex-row flex-wrap ms-md-auto">
                <li class="nav-item d-flex">
                  <RouterLink to="/login" class="nav-link col-6 col-lg-auto">Ingresar</RouterLink>
                </li>
              </ul>
            </div>
          </div>
        </nav>

    </div>
  </div>
  <div v-else>
    <b-card-text>
     Error conectando al servidor no se presentan datos
    </b-card-text>
  </div>

</template>

<script>
import { RouterLink} from 'vue-router'
//https://www.positronx.io/handle-ajax-requests-in-vue-js-with-axios-fetch-api/
//https://www.koderhq.com/tutorial/vue/http-axios/
//https://www.bezkoder.com/vue-axios-example/
import http from "../http-common";

export default {
  
  data() {
    return {
      vgetHead: [],
      logo_img: null,
    }
  },
  mounted() {
    this.getHead();
  },
  methods: {
    fortmatResponse(res) {
      return JSON.stringify(res, null, 2);
    },
    async getHead() {
      try {
        const res = await http.get("api/conjunto/listar/1");
        const result = {
          status: res.status + "-" + res.statusText,
          //headers: res.headers,
          data: res.data[0],
        };
        this.vgetHead.push(result),
        this.logo_img= result.data.logo
      } catch (err) {
        this.vgetHead.push(this.fortmatResponse(err.response?.data) || err);
        //this.getResult = this.fortmatResponse(err.response?.data) || err;
      }
    },
    clearGetOutput() {
      this.vgetHead = null;
    },
  }
};

</script>


<style scoped>


</style>