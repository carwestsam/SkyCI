<template>
    <div>
        <div>
            Build {{$route.params.pipeline_id}}
        </div>
        <div v-for="build in builds" :key="build.id">
            <h2>{{build.buildIndex}}</h2>
            <p>{{build.state}}</p>
            <p>id: {{build.id}}</p>
            <p>pipeline id: {{build.pipelineId}}</p>
            <pre>{{build.configFile}}</pre>
        </div>
    </div>
</template>
<script>
export default {
    name: 'build',
    data () {
        return {
            builds: []
        }
    },
    created: function () {
        this.refreshList()
    },
    methods: {
        refreshList: function () {
                    this.$http.get('/build/' + this.$route.params.pipeline_id)
            .then((resp) => {
                this.builds = resp.data.content
            }).catch((error) => {
                console.log(error)
            })
        }
    }
}
</script>
<style>

</style>
