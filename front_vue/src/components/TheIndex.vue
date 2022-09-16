<template >
  <div v-if="vgetDatos">
  <div v-for="resultb in vgetDatos" :key="resultb.data.id">
  <!-- Masthead-->

  <header>
  <!-- Navbar -->
  <nav class="navbar navbar-expand-lg navbar-light bg-white">
    <div class="container-fluid">
      <button
        class="navbar-toggler"
        type="button"
        data-mdb-toggle="collapse"
        data-mdb-target="#navbarExample01"
        aria-controls="navbarExample01"
        aria-expanded="false"
        aria-label="Toggle navigation"
      >
        <i class="fas fa-bars"></i>
      </button>
      <div class="collapse navbar-collapse" id="navbarContent">
            <ul class="navbar-nav ml-auto">
                <li class="nav-item dropdown">
                    <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-bs-toggle="dropdown" aria-expanded="false"> Acciones </a>
                    <ul class="dropdown-menu dropdown-menu-end" aria-labelledby="navbarDropdown">
                        <li><a class="dropdown-item" href="#">Ingresar</a></li>
                    </ul>
                </li>
            </ul>
        </div>
    </div>
  </nav>
  <!-- Navbar -->

  <!-- Background image -->
  <div class="p-5 text-center bg-image" :style="backgroundImageInlineStyle">
    <div class="mask" style="background-color: rgba(0, 0, 0, 0.6);">
      <div class="d-flex justify-content-center align-items-center h-100">
        <div class="text-white">
          <h1 class="mb-3">{{resultb.data.name}}</h1>
          <h4 class="mb-3">{{resultb.data.eslogan}}</h4>
        </div>
      </div>
    </div>
  </div>
    <!-- Background image -->
  </header>

        <!-- Section Noticias-->
          <b-row>
            <b-col>
              <h2 class="page-section-heading text-center text-uppercase text-secondary mb-0">Noticias</h2>
            </b-col>
          </b-row>
          <b-row>
            <b-col>
              <cnoticias></cnoticias>
            </b-col>
          </b-row>
        
        <!-- Section Sección avisos ventas-->
          <b-row>
            <b-col>
              <h2 class="page-section-heading text-center text-uppercase text-secondary mb-0">Propiedades en Venta</h2>
            </b-col>
            <b-col>
              <h2 class="page-section-heading text-center text-uppercase text-secondary mb-0">Propiedades en Arriendo</h2>
            </b-col>
          </b-row>
          <b-row>
            <b-col>
              <cpropiedadventa></cpropiedadventa>
            </b-col>
            <!-- Section Sección avisos arriendo-->
            <b-col>
              <cpropiedadarriendo></cpropiedadarriendo>
            </b-col>
          </b-row>
        <!-- Section Sección avisos portafolio-->
          <b-row>
            <h2 class="page-section-heading text-center text-uppercase text-secondary mb-0">Portafolio</h2>
          </b-row>
          <b-row>
            <b-col>
              <cportafolio></cportafolio>
            </b-col>
          </b-row>
        <!-- About Section-->
        <b-row>
            <b-col>
              <section class="page-section bg-primary text-white mb-0" id="about">
                <!-- About Section Heading-->
                <h2 class="page-section-heading text-center text-uppercase text-white">Acerca de nosotros</h2>
                <!-- Icon Divider-->
                <div class="divider-custom divider-light">
                    <div class="divider-custom-line"></div>
                    <div class="divider-custom-icon"><i class="fas fa-star"></i></div>
                    <div class="divider-custom-line"></div>
                </div>
                <!-- About Section Content-->
                <div class="row">
                    <div class="col-sm12"><p class="lead">{{resultb.data.about}}</p></div>
                </div>
              </section>
            </b-col>
          </b-row>
        <!-- Section salon comunal-->
          <b-row>
            <h2 class="page-section-heading text-center text-uppercase text-secondary mb-0">Salón Comunal</h2>
          </b-row>
          <b-row>
            <b-col>
              <csaloncomunal></csaloncomunal>
            </b-col>
          </b-row>
          <!-- Contact Section-->
          <!-- Contact Section Heading-->
          <b-row>
            <b-col>
             <h2 class="page-section-heading text-center text-uppercase text-secondary mb-0">Contactenos</h2>
            </b-col>
          </b-row>
          <b-row>
            <b-col sm="12" lg="6">
                <b-row>
                  <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d3976.5243435300504!2d-74.16923798590985!3d4.678527543153759!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x8e3f9cfcc94cae0d%3A0x5335f540b66e675c!2sConjunto%20Senderos%20De%20La%20Estancia%201!5e0!3m2!1ses-419!2sco!4v1656821072384!5m2!1ses-419!2sco" width="600" height="450" style="border:0;" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade"></iframe>
                </b-row>
                <b-row class="text-center">
                  <b-col sm="4" lg="4" class="float-start">
                    <a href="#" id="around">
                      <i class="bi bi-house-door-fill"></i>
                    </a>
                    <p class="lead">{{resultb.data.adress}}</p>
                  </b-col>
                  <b-col sm="4" lg="4" class="float-start">
                    <a href="#" id="around">
                      <i class="bi bi-inbox-fill"></i>
                    </a>
                    <p class="lead">{{resultb.data.email}}</p>
                  </b-col>
                  <b-col sm="4" lg="4" class="float-start">
                    <a href="#" id="around">
                      <i class="bi bi-telephone-inbound-fill"></i>
                    </a>
                    <p class="lead">{{resultb.data.telephone}}</p>
                  </b-col>
                </b-row>
            </b-col>
              <b-col sm="12" lg="6">
                <form id="contactForm" data-sb-form-api-token="API_TOKEN">
                        <!-- Name input-->
                        <div class="form-floating mb-3">
                            <input class="form-control" id="name" type="text" placeholder="Enter your name..." data-sb-validations="required" />
                            <label for="name">Nombres y Apellidos</label>
                            <div class="invalid-feedback" data-sb-feedback="name:required">El campo es requerido</div>
                        </div>
                        <!-- Email address input-->
                        <div class="form-floating mb-3">
                            <input class="form-control" id="email" type="email" placeholder="name@example.com" data-sb-validations="required,email" />
                            <label for="email">Correo</label>
                            <div class="invalid-feedback" data-sb-feedback="email:required">El campo es requerido</div>
                            <div class="invalid-feedback" data-sb-feedback="email:email">Email is not valid.</div>
                        </div>
                        <!-- Phone number input-->
                        <div class="form-floating mb-3">
                            <input class="form-control" id="phone" type="tel" placeholder="(123) 456-7890" data-sb-validations="required" />
                            <label for="phone">Teléfono</label>
                            <div class="invalid-feedback" data-sb-feedback="phone:required">El campo es requerido.</div>
                        </div>
                        <!-- Message input-->
                        <div class="form-floating mb-3">
                            <textarea class="form-control" id="message" type="text" placeholder="Enter your message here..." style="height: 10rem" data-sb-validations="required"></textarea>
                            <label for="message">Mensaje</label>
                            <div class="invalid-feedback" data-sb-feedback="message:required">El campo es requerido.</div>
                        </div>
                        <!-- Submit success message-->
                        <!---->
                        <!-- This is what your users will see when the form-->
                        <!-- has successfully submitted-->
                        <div class="d-none" id="submitSuccessMessage">
                            <div class="text-center mb-3">
                                <div class="fw-bolder">Formulario enviado satisfactoriamente</div>
                                <br />
                                <a href="https://startbootstrap.com/solution/contact-forms">https://startbootstrap.com/solution/contact-forms</a>
                            </div>
                        </div>
                        <!-- Submit error message-->
                        <!---->
                        <!-- This is what your users will see when there is-->
                        <!-- an error submitting the form-->
                        <div class="d-none" id="submitErrorMessage"><div class="text-center text-danger mb-3">Error enviando mensaje!</div></div>
                        <!-- Submit Button-->
                        <button class="btn btn-primary btn-xl disabled" id="submitButton" type="submit">Enviar</button>
                    </form>
              </b-col>
          </b-row>
          <!-- Icon Divider-->
          <div class="divider-custom">
              <div class="divider-custom-line"></div>
              <div class="divider-custom-icon"><i class="fas fa-star"></i></div>
              <div class="divider-custom-line"></div>
          </div>
          <!-- Contact Section Form-->
          <div class="row justify-content-center">
              <div class="col-lg-8 col-xl-7"> </div>
          </div>
        <br/>
    </div>
  </div>
  <div v-else>
    <b-card-text>
     Error conectando al servidor no se presentan datos
    </b-card-text>
  </div>
</template>

<script>
import http from "../http-common";
import cnoticias from './CarouselNoticias.vue';
import cpropiedadventa from './CarouselPropiedadesventa.vue';
import cpropiedadarriendo from './CarouselPropiedadesarriendo.vue';
import cportafolio from './CarouselPortafolio.vue';
import csaloncomunal from './SalonComunal.vue';

export default {
  data() {
    return {
      vgetDatos: [],
    }
  },
  mounted() {
    this.getDatos();
  },
  methods: {
    fortmatResponse(res) {
      return JSON.stringify(res, null, 2);
    },
    async getDatos() {
      try {
        const res = await http.get("api/conjunto/listar/1");
        const result = {
          status: res.status + "-" + res.statusText,
          //headers: res.headers,
          data: res.data,
        };
        this.vgetDatos.push(result);
      } catch (err) {
        this.vgetDatos.push(this.fortmatResponse(err.response?.data) || err);
      }
    },
    clearGetOutput() {
      this.vgetDatos = null;
      this.noticias = null;
    },
  },
  components: {
    cnoticias,
    cpropiedadventa,
    cpropiedadarriendo,
    cportafolio,
    csaloncomunal,
  },
  computed: {
    backgroundImageInlineStyle () {
      //return `height: 50px;`;
      //return `background-image: url("${this.result}");`;
      return `background-image: url("${this.vgetDatos[0].data.imagen}"); height: auto; background-repeat: no-repeat;`;
    }
  },
};
</script>

<style>
.row {
  --bs-gutter-x: -1.5rem !important;
}

#around {
  background-color: cornflowerblue;
  border: none;
  color: white;
  padding: 20px;
  justify-content: center;
  line-height: 5px;
  display: inline-block;
  font-size: 30px;
  border-radius: 100%;
  width: 30%;
  box-shadow: 0 1rem 1rem rgba(0, 0, 0, 0.175) !important;
  margin-top: 10px;
  display: inline-flex;
  justify-content: center;
  align-items: center;
}

.navbar-nav {
  margin-left: auto !important;
}

.col-lg-6 {
    padding: 0.5em 0.5em !important;
  }
</style>
