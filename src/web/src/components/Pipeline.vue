<template>
    <div>
        <form>
            <label for="pl_name">Pipeline Name </label><input type="text" id="pl_name" v-model="pl_name"><br>
            <label for="pl_git">Git Repo</label><input type="text" id="pl_git" v-model="pl_git"><br>
            <label for="pl_path">Build file name</label><input type="text" id="pl_path" v-model="pl_path"><br>
            <input type="submit" value="submit" @click="createPipeline()">
        </form>
        <div class="pipeline" v-for="pl in pipelines" :key="pl.id">
            <h3>{{pl.name}}</h3>
            <h5>{{pl.status}}</h5>
            <code>{{pl.gitUrl}}</code>
            <h5>{{pl.id}}</h5>
            <h5><router-link :to="`/build/${pl.id}`">Details</router-link></h5>
            <input type="submit" value="delete" @click="deletePipeline(pl.id)">
            <input type="submit" value="build" @click="triggerPipeline(pl.id)">
        </div>
    </div>
</template>

<script>
// import Router from 'vue-router'
export default {
    data () {
        return {
            pl_name: "example",
            pl_git: "https://github.com/carwestsam/skyci-project-examples.git",
            pl_path: "/build.yml",
            pipelines: [
                {
                }
            ]
        }
    },
    created: function () {
        this.refreshList()
    },
    methods: {
        createPipeline: function () {
            this.$http.post('/pipeline/', {
                "type": 'default',
                "name": this.pl_name,
                "gitUrl": this.pl_git,
                "ciCfgPath": this.pl_path
            }).then((response) => {
                console.log(response)
            }).then(()=>{
                this.refreshList()
            })
        },
        refreshList: function () {
            this.$http.get('/pipeline')
                .then((response) => {
                    console.log(response.data.content)
                    this.pipelines = response.data.content
                })
        },
        deletePipeline: function (pipelineId) {
            this.$http.delete('/pipeline/pl/'+pipelineId)
                .then((response) => {
                    console.log(response)
                }).then(()=>{
                    this.refreshList()
                })
        },
        triggerPipeline: function (pipelineId) {
            this.$http.get('/pipeline/' + pipelineId + '/build')
                .then((response) => {
                    console.log(response.data)
                }).then(()=> {
                    this.refreshList()
                })
        }
    }
}
</script>

<style>
.pipeline{
    text-align: left;
    border-bottom: 1px solid black;
}
</style>
