<template>
    <div>
        <b-row>
            <b-col sm="12" lg="6">
              <b-row>
                <div class="text-center section">
                    <h2 class="h2">Salon comunal 1</h2>
                    <p class="text-lg font-medium text-gray-600 mb-6">
                    Fechas de sepacración y/o actividades comunales
                    </p>
                    <v-calendar
                    class="custom-calendar max-w-full"
                    :masks="masks"
                    :attributes="attributes"
                    disable-page-swipe
                    is-expanded
                    >
                    <template v-slot:day-content="{ day, attributes }">
                        <div class="flex flex-col h-full z-10 overflow-hidden">
                        <span class="day-label text-sm text-gray-900">{{ day.day }}</span>
                        <div class="flex-grow overflow-y-auto overflow-x-auto">
                            <p
                            v-for="attr in attributes"
                            :key="attr.key"
                            class="text-xs leading-tight rounded-sm p-1 mt-0 mb-1"
                            :class="attr.customData.class"
                            >
                            {{ attr.customData.title }}
                            </p>
                        </div>
                        </div>
                    </template>
                    </v-calendar>
                </div>
              </b-row>
              <b-row>
                <div id="carouselSaloncomunal" class="carousel slide" data-bs-ride="carousel">
                    <div class="carousel-indicators">
                    <button type="button" data-bs-target="#carouselSaloncomunal" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
                    <button type="button" data-bs-target="#carouselSaloncomunal" data-bs-slide-to="1" aria-label="Slide 2"></button>
                    <button type="button" data-bs-target="#carouselSaloncomunal" data-bs-slide-to="2" aria-label="Slide 3"></button>
                    </div>
                    <div class="carousel-inner">
                    <div class="carousel-item active">
                        <img src="https://picsum.photos/600/300/?image=25" class="d-block w-100" alt=" ">
                        <div class="carousel-caption d-none d-md-block">
                        <h5>First slide label</h5>
                        <p>Some representative placeholder content for the first slide.</p>
                        </div>
                    </div>
                    <div class="carousel-item">
                        <img src="https://placekitten.com/1000/300" class="d-block w-100" alt="...">
                        <div class="carousel-caption d-none d-md-block">
                        <h5>Second slide label</h5>
                        <p>Some representative placeholder content for the second slide.</p>
                        </div>
                    </div>
                    <div class="carousel-item">
                        <img src="https://placekitten.com/300/300" class="d-block w-100" alt="...">
                        <div class="carousel-caption d-none d-md-block">
                        <h5>Third slide label</h5>
                        <p>Some representative placeholder content for the third slide.</p>
                        </div>
                    </div>
                    </div>
                    <button class="carousel-control-prev" type="button" data-bs-target="#carouselSaloncomunal" data-bs-slide="prev">
                    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                    <span class="visually-hidden">Previous</span>
                    </button>
                    <button class="carousel-control-next" type="button" data-bs-target="#carouselSaloncomunal" data-bs-slide="next">
                    <span class="carousel-control-next-icon" aria-hidden="true"></span>
                    <span class="visually-hidden">Next</span>
                    </button>
                </div>
              </b-row>
            </b-col>
            <b-col sm="12" lg="6">
              <div class="text-center section">
                    <h2 class="h2">Salon comunal 1</h2>
                    <p class="text-lg font-medium text-gray-600 mb-6">
                    Fechas de sepacración y/o actividades comunales
                    </p>
                    <v-calendar
                    class="custom-calendar max-w-full"
                    :masks="masks"
                    :attributes="attributes"
                    disable-page-swipe
                    is-expanded
                    >
                    <template v-slot:day-content="{ day, attributes }">
                        <div class="flex flex-col h-full z-10 overflow-hidden">
                        <span class="day-label text-sm text-gray-900">{{ day.day }}</span>
                        <div class="flex-grow overflow-y-auto overflow-x-auto">
                            <p
                            v-for="attr in attributes"
                            :key="attr.key"
                            class="text-xs leading-tight rounded-sm p-1 mt-0 mb-1"
                            :class="attr.customData.class"
                            >
                            {{ attr.customData.title }}
                            </p>
                        </div>
                        </div>
                    </template>
                    </v-calendar>
                </div>
                <div id="carouselSaloncomunal" class="carousel slide" data-bs-ride="carousel">
                    <div class="carousel-indicators">
                    <button type="button" data-bs-target="#carouselSaloncomunal" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
                    <button type="button" data-bs-target="#carouselSaloncomunal" data-bs-slide-to="1" aria-label="Slide 2"></button>
                    <button type="button" data-bs-target="#carouselSaloncomunal" data-bs-slide-to="2" aria-label="Slide 3"></button>
                    </div>
                    <div class="carousel-inner">
                    <div class="carousel-item active">
                        <img src="https://picsum.photos/600/300/?image=25" class="d-block w-100" alt=" ">
                        <div class="carousel-caption d-none d-md-block">
                        <h5>First slide label</h5>
                        <p>Some representative placeholder content for the first slide.</p>
                        </div>
                    </div>
                    <div class="carousel-item">
                        <img src="https://placekitten.com/1000/300" class="d-block w-100" alt="...">
                        <div class="carousel-caption d-none d-md-block">
                        <h5>Second slide label</h5>
                        <p>Some representative placeholder content for the second slide.</p>
                        </div>
                    </div>
                    <div class="carousel-item">
                        <img src="https://placekitten.com/300/300" class="d-block w-100" alt="...">
                        <div class="carousel-caption d-none d-md-block">
                        <h5>Third slide label</h5>
                        <p>Some representative placeholder content for the third slide.</p>
                        </div>
                    </div>
                    </div>
                    <button class="carousel-control-prev" type="button" data-bs-target="#carouselSaloncomunal" data-bs-slide="prev">
                    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                    <span class="visually-hidden">Previous</span>
                    </button>
                    <button class="carousel-control-next" type="button" data-bs-target="#carouselSaloncomunal" data-bs-slide="next">
                    <span class="carousel-control-next-icon" aria-hidden="true"></span>
                    <span class="visually-hidden">Next</span>
                    </button>
                </div>
            </b-col>
        </b-row>
    </div>

  

</template>

<script>
export default {
  data() {
    const month = new Date().getMonth();
    const year = new Date().getFullYear();
    return {
      masks: {
        weekdays: "WWW",
      },
      attributes: [
        {
          key: 1,
          customData: {
            title: "Lunch with mom.",
            class: "bg-red-600 text-white",
          },
          dates: new Date(year, month, 1),
        },
        {
          key: 2,
          customData: {
            title: "Take Noah to basketball practice",
            class: "bg-blue-500 text-white",
          },
          dates: new Date(year, month, 2),
        },
        {
          key: 3,
          customData: {
            title: "Noah's basketball game.",
            class: "bg-blue-500 text-white",
          },
          dates: new Date(year, month, 5),
        },
        {
          key: 4,
          customData: {
            title: "Take car to the shop",
            class: "bg-indigo-500 text-white",
          },
          dates: new Date(year, month, 5),
        },
        {
          key: 4,
          customData: {
            title: "Meeting with new client.",
            class: "bg-teal-500 text-white",
          },
          dates: new Date(year, month, 7),
        },
        {
          key: 5,
          customData: {
            title: "Mia's gymnastics practice.",
            class: "bg-pink-500 text-white",
          },
          dates: new Date(year, month, 11),
        },
        {
          key: 6,
          customData: {
            title: "Cookout with friends.",
            class: "bg-orange-500 text-white",
          },
          dates: { months: 5, ordinalWeekdays: { 2: 1 } },
        },
        {
          key: 7,
          customData: {
            title: "Mia's gymnastics recital.",
            class: "bg-pink-500 text-white",
          },
          dates: new Date(year, month, 22),
        },
        {
          key: 8,
          customData: {
            title: "Visit great grandma.",
            class: "bg-red-600 text-white",
          },
          dates: new Date(year, month, 25),
        },
      ],
    };
  },
};
</script>

<style scoped>
</style>