<template>
    <v-container fluid id='about-container'>
        <h1><strong>About BGC-Miner</strong></h1>
        <br>
        <p>BGC-Miner allows the visualization, annotation and analysis of bacterial biosynthetic gene clusters. It intergrates
            several <i>in-silico</i> tools.
        </p>
        <p>BGC-Miner is powered by several open source tools;
            <ul><br>
                <li><a href="https://pypi.org/project/biovec/" target="_blank">BioVec</a></li>
                <li><a href="https://umap-learn.readthedocs.io/en/latest/" target="_blank">UMAP</a></li>
                <li><a href="https://sklearn.org/" target="_blank">scikit-learn</a></li>
                <li><a href="" target="_blank">Tensorflow</a></li>
                <li><a href="" target="_blank">Protein Visualization Library</a></li>
            </ul>
        </p>
        <h1><strong>How to Cite</strong></h1>
        <p></p>
    </v-container>
</template>

<style scoped>
    #about-container{
        margin-top: 2.5%;
        width: 80%;
    }
    ul > li {
        list-style-type: none;
    }
</style>

<script>

export default{
    name: 'AboutComponent',
    components: {

    },
    data(){
        return {
            
        }
    }
}
</script>
