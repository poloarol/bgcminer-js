<template>
    <v-container>
        <v-form v-model='validate' id='retrieve-form'>
            <v-row>
                <v-container>
                    <v-text-field
                        label='Job ID'
                        v-model='job_id'
                        :rules='jobRules'
                        required
                    >
                    </v-text-field>
                </v-container>
            </v-row>
            <v-btn class="mr-4" @click='submit'>Retrieve</v-btn>
        </v-form>
    </v-container>
</template>

<style scoped>
    #retrieve-form{
        margin-top: 15%;
    }
</style>

<script>

export default{
    name: 'RetrievalComponent',
    components: {

    },
    data(){
        return {
            job_id: '',
            validate: '',
            jobRules: [
                v => !!v || 'Name is required',
                 v => (v && v.length <= 10) || 'Name must be less than 10 characters',
          ],
        }
    },
    methods: {
        submit(){

        }
    }
}
</script>
