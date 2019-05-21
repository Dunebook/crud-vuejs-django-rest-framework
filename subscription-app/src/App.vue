<template>
  <div class="container">
    <div class="row justify-content-center">
      <div class="col-md-8">
        <h2><router-link to="/index">Subscriptions</router-link></h2>
        <router-link to="/create" class="btn btn-sm btn-primary">Add subscription</router-link>

        <router-view />
      </div>
    </div>
  </div>
</template>
