<template>
  <div class="error-bg">
    <div class="error-page error-box">
      <h1 class="headline text-blue">:(</h1>
      <div class="error-content">
        <h2>
          <i class="fa fa-warning text-blue"></i>
          Oops! This tenant is not yet created!
        </h2>
        <p>
          If you are interested in buying this tenant go to our landing page.
        </p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'inactive-tenant'
}
</script>

<style>
.error-bg {
  display: flex;
  height: 100vh;
}
.error-box {
  margin: 10% auto;
}
.error-content {
  text-align: center;
}
</style>
