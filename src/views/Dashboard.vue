<template>
  <div class="container mx-auto">
    <!-- start of container setup -->
    <div class="main-content flex-1 bg-gray-100 mt-12 md:mt-2 pb-18 md:pb-5">
      <div class="flex flex-wrap">
        <div class="w-full md:w-1/2 xl:w-1/3 p-6">
          <!--Metric Card-->
          <div
            class="
              bg-gradient-to-b
              from-green-200
              to-green-100
              border-b-4 border-green-600
              rounded-lg
              shadow-xl
              p-5
            "
          >
            <div class="flex flex-row items-center">
              <div class="flex-shrink pr-4">
                <div class="rounded-full p-5 bg-green-600">
                  <i class="fa fa-wallet fa-2x fa-inverse"></i>
                </div>
              </div>
              <div class="flex-1 text-right md:text-center">
                <h5 class="font-bold uppercase text-gray-600">Total Sensors Record Counts</h5>
                <h3 class="font-bold text-3xl">
                  15
                  <span class="text-green-500"
                    ><i class="fas fa-caret-up"></i
                  ></span>
                </h3>
              </div>
            </div>
          </div>
          <!--/Metric Card-->
        </div>
        <div class="w-full md:w-1/2 xl:w-1/3 p-6">
          <!--Metric Card-->
          <div
            class="
              bg-gradient-to-b
              from-pink-200
              to-pink-100
              border-b-4 border-pink-500
              rounded-lg
              shadow-xl
              p-5
            "
          >
            <div class="flex flex-row items-center">
              <div class="flex-shrink pr-4">
                <div class="rounded-full p-5 bg-pink-600">
                  <i class="fas fa-users fa-2x fa-inverse"></i>
                </div>
              </div>
              <div class="flex-1 text-right md:text-center">
                <h5 class="font-bold uppercase text-gray-600">Total Sensors</h5>
                <h3 class="font-bold text-3xl">
                  5
                  <span class="text-pink-500"
                    ><i class="fas fa-exchange-alt"></i
                  ></span>
                </h3>
              </div>
            </div>
          </div>
          <!--/Metric Card-->
        </div>
        <div class="w-full md:w-1/2 xl:w-1/3 p-6">
          <!--Metric Card-->
          <div
            class="
              bg-gradient-to-b
              from-yellow-200
              to-yellow-100
              border-b-4 border-yellow-600
              rounded-lg
              shadow-xl
              p-5
            "
          >
            <div class="flex flex-row items-center">
              <div class="flex-shrink pr-4">
                <div class="rounded-full p-5 bg-yellow-600">
                  <i class="fas fa-user-plus fa-2x fa-inverse"></i>
                </div>
              </div>
              <div class="flex-1 text-right md:text-center">
                <h5 class="font-bold uppercase text-gray-600">Working Sensors</h5>
                <h3 class="font-bold text-3xl">
                  2
                  <span class="text-yellow-600"
                    ><i class="fas fa-caret-up"></i
                  ></span>
                </h3>
              </div>
            </div>
          </div>
          <!--/Metric Card-->
        </div>
      </div>
    </div>
  </div>
  <!-- end of container setup -->
</template>

<script>
export default {
  name: "Home",
  components: {},
};
</script>
