<template>
  <b-row>
  <b-col sm="12">
  <div class="card-centrada">
    <b-card
      title="Login"
      align="center"
    >
      <b-card-text>
        
        <div>
          <b-form @submit="onSubmit" @reset="onReset" v-if="show">
          <b-form-group
              id="input-group-1"
              label="nombres:"
              label-for="nombres"
            >
              <b-form-input
                id="nombre"
                v-model="form.user"
                type="text"
                placeholder="Nombres"
                required
              ></b-form-input>
            </b-form-group>
            <b-form-group
              id="input-group-1"
              label="apeliidos:"
              label-for="apellidos"
            >
              <b-form-input
                id="apellidos"
                v-model="form.user"
                type="text"
                placeholder="Apellidos"
                required
              ></b-form-input>
            </b-form-group>
            <b-form-group
              id="input-group-1"
              label="correo:"
              label-for="correo"
            >
              <b-form-input
                id="correo"
                v-model="form.user"
                type="text"
                placeholder="Correo"
                required
              ></b-form-input>
            </b-form-group>
            <b-form-group
              id="input-group-1"
              label="telefono:"
              label-for="telefono"
            >
              <b-form-input
                id="telefono"
                v-model="form.user"
                type="text"
                placeholder="Teléfono"
                required
              ></b-form-input>
            </b-form-group>
            <b-form-group
              id="input-group-1"
              label="propiedad:"
              label-for="propiedad"
            >
              <b-form-input
                id="propiedad"
                v-model="form.user"
                type="text"
                placeholder="Propiedad"
                required
              ></b-form-input>
            </b-form-group>
            <b-form-group
              id="input-group-1"
              label="usuario:"
              label-for="usuario"
            >
              <b-form-input
                id="usuario"
                v-model="form.user"
                type="text"
                placeholder="Usuario"
                required
              ></b-form-input>
            </b-form-group>
             <b-form-group id="input-group-4" v-slot="{ ariaDescribedby }">
              <b-form-checkbox-group
                v-model="form.checked"
                id="checkboxes-4"
                :aria-describedby="ariaDescribedby"
              >
                <b-form-checkbox value="that">Activo</b-form-checkbox>
              </b-form-checkbox-group>
            </b-form-group>
            <b-button type="submit" variant="primary">Registrar</b-button>
          </b-form>
          <hr/>
          <RouterLink to="/register" class="">Ingresar</RouterLink>
          <p></p>
          <RouterLink to="/recoverypass" class="">Recuperar contraseña</RouterLink>
        </div>
      </b-card-text>
      </b-card>
    </div>
    </b-col>
  </b-row>

</template>

<script>
  export default {
    data() {
      return {
        form: {
          email: '',
          name: '',
          food: null,
          checked: []
        },
        foods: [{ text: 'Select One', value: null }, 'Carrots', 'Beans', 'Tomatoes', 'Corn'],
        show: true
      }
    },
    methods: {
      onSubmit(event) {
        event.preventDefault()
        alert(JSON.stringify(this.form))
      },
      onReset(event) {
        event.preventDefault()
        // Reset our form values
        this.form.email = ''
        this.form.name = ''
        this.form.food = null
        this.form.checked = []
        // Trick to reset/clear native browser form validation state
        this.show = false
        this.$nextTick(() => {
          this.show = true
        })
      }
    }
  }
</script>

<style scoped>
.card-centrada {
  background-color: #fff;
	border-radius: 4px;
	max-width: 400px;
	margin: 5% auto;
	height: auto;/*100px;*/
	position: relative;
	padding: 34px;
	color: #444;
	cursor: pointer;
}

@media (min-width: 1024px) {
}


</style>
