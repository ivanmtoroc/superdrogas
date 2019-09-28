<template>
  <div class="row">
    <div class="col-md-12">
      <div id="carousel" class="carousel slide" data-ride="carousel">
        <ol class="carousel-indicators">
          <li data-target="#carousel" data-slide-to="0" class="active"></li>
          <li data-target="#carousel" data-slide-to="1"></li>
          <li data-target="#carousel" data-slide-to="2"></li>
        </ol>
        <div class="carousel-inner">
          <div class="item active">
            <img src="@/static/images/ad-01.jpg" alt="Ad">
          </div>
          <div class="item">
            <img src="@/static/images/ad-02.png" alt="Ad">
          </div>
          <div class="item">
            <img src="@/static/images/ad-03.jpg" alt="Ad">
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'carousel'
}
</script>
