<template>
    <div>
        <form>
            <label for="pl_name">Pipeline Name </label><input type="text" id="pl_name" v-model="pl_name"><br>
            <label for="pl_git">Git Repo</label><input type="text" id="pl_git" v-model="pl_git"><br>
            <label for="pl_path">Build file name</label><input type="text" id="pl_path" v-model="pl_path"><br>
            <input type="submit" value="submit" @click="createPipeline()">
        </form>
        <div class="pipeline" v-for="pl in pipelines">
            <h3>{{pl.name}}</h3>
            <h5>{{pl.status}}</h5>
            <code>{{pl.gitUrl}}</code>
            <h5>{{pl.id}}</h5>
            <input type="submit" value="delete" @click="deletePipeline(pl.id)">
        </div>
    </div>
</template>

<script>
export default {
    data () {
        return {
            pl_name: "",
            pl_git: "",
            pl_path: "",
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
            console.log('x')
            this.$http.delete('/pipeline/pl/'+pipelineId)
                .then((response) => {
                    console.log(response)
                }).then(()=>{
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
