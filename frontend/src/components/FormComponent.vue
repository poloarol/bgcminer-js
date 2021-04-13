<template>
  <v-form v-model='valid' id='main-form'>
    <v-container>
      <v-row>
        <v-select
          :items='items'
          label='Models'
          :rules="[v => !!v || 'Item is required']"
          outlined
        >
        </v-select>
      </v-row>
      <v-row>
      </v-row>
      <v-row>
        <v-file-input
          accept='.gbk'
          label='GenBank file'
          multiple
          outlined
        >
        </v-file-input>
      </v-row>
      <br><br>
      <v-btn class='mr-4' @click="submit"> Analyze data </v-btn>
      <v-btn class='mr-4' @click='reset'> Clear form </v-btn>
    </v-container>
  </v-form>
</template>

<style scoped>
  #main-form {
    margin-top: 7%;
  }
</style>

<script>

export default{
  name: 'FormComponent',
  props: [],
  components: {},

  data() {
    return {
      email: '',
      bgc: '',
      valid: false,
      items: ['Random Forest', 'AdaBoost + Random Forest', 'k-Nearest Neighbour', 'MultiLayer Perceptron', 'All'],
      emailRules: [
        v => !!v || 'E-mail is required',
        v => /.+@.+/.test(v) || 'E-mail must be valid',
      ],
    }
  },

  computed: {
    isFile() {
      if(this.bgc === '')
        return true
      return false
    },

    isBGC() {
      if(this.file === '')
        return true
      return false
    }
  },

  methods: {
    validate(){
      this.$refs.form.validate()
    },
    reset(){
      this.$refs.form.reset()
    },
    submit(){
      this.validate()
      console.log(this.valid)
    }
  }
}

</script>
