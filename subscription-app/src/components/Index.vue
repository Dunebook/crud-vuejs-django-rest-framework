<template>
    <div class="pt-5">
        <div v-if="subscriptions && subscriptions.length">
            <div class="card mb-3" v-for="subscription of subscriptions" v-bind:key="subscription.id">
                <div class="row no-gutters">
                    <div class="col-md-4">
                        <svg class="bd-placeholder-img" width="200" xmlns="http://www.w3.org/2000/svg" preserveAspectRatio="xMidYMid slice" focusable="false" role="img" aria-label="Placeholder: Thumbnail"><title>{{ subscription.name }}</title><rect width="100%" height="100%" fill="#55595c"/><text x="50%" y="50%" fill="#eceeef" dy=".3em">{{ subscription.name.charAt(0) }}</text></svg>
                    </div>
                    <div class="col-md-8">
                        <div class="card-body">
                            <h5 class="card-title">{{ subscription.name }}</h5>
                            <p class="card-text">{{ subscription.description }}</p>
                            <router-link :to="{name: 'edit', params: { id: subscription.id }}" class="btn btn-sm btn-primary">Edit</router-link>
                            <button class="btn btn-danger btn-sm ml-1" v-on:click="deleteSubscription(subscription)">Delete</button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <p  v-if="subscriptions.length == 0">No subscriptions</p>
    </div>
</template>
<script>

import axios from 'axios';

export default {
    data() {
        return {
            subscriptions: []
        }
    },
    created() {
        this.all();
    },
    methods: {
        deleteSubscription: function(subscr) {
            if (confirm('Delete ' + subscr.name)) {
                axios.delete(`http://127.0.0.1:8000/api/subscriptions/${subscr.id}`)
                    .then( response => {
                        this.all();
                    });
            }
        },
        all: function () {
            axios.get('http://127.0.0.1:8000/api/subscriptions/')
                .then( response => {
                    this.subscriptions = response.data
                });
        }
    },
}
</script>