<template>
  <v-app>
      <v-app-bar app color="#830E0D" dark>
        <div class="d-flex align-center">
          <v-img
            alt="uOttawa Logo"
            class="shrink mr-2"
            contain
            src="./assets/uottawa_white.png"
            transition="scale-transition"
            width="160"
            />
        </div>
        <v-spacer></v-spacer>
        <v-btn
          href="http://boddylab.ca/"
          target="_blank"
          text>
          <span class="mr-2">Boddy Lab</span>
          <v-icon>mdi-open-in-new</v-icon>
        </v-btn>
    </v-app-bar>
    <v-main>
      <router-view></router-view>
    </v-main>
    <v-footer dark padless id='main-footer'>
      <v-card flat tile class="lighten-1 white--text text-center" id='sec-footer'>
        <v-card-text>
          <v-btn
            v-for='(icon, index) in icons'
            :key=index
            class="mx-4 white--text"
            icon
            :href=links[index]
            target='_blank'
          ><v-icon>{{ icon }}</v-icon></v-btn>
        </v-card-text>
        <v-card-text>Welcome to the Boddy lab</v-card-text>
        <v-divider></v-divider>
        <v-card-text>
          <v-icon>{{ 'mdi-copyright' }}</v-icon> {{ new Date().getFullYear() }} - <strong>Boddy Lab</strong>
        </v-card-text>
      </v-card>
    </v-footer>
  </v-app>
</template>

<style scoped>
  #main-footer{
    bottom: 0;
    position: abs;
    width: 100%;
  }
  #sec-footer{
    width: 100%;
  }
</style>

<script>

export default {
  name: 'App',
  components: {
  },
  data: () => ({
    icons: ['mdi-twitter', 'mdi-linkedin', 'mdi-web'],
    links: ['https://twitter.com/BoddyLab', 'https://www.linkedin.com/in/chris-boddy-1742976/', 'http://boddylab.ca/']
  }),
}

</script>
