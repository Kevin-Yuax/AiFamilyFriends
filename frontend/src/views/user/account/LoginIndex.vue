<script setup>

</script>

<template>
  <div class="flex justify-center mt-80">
     <fieldset class="fieldset bg-white/90 backdrop-blur-sm border border-indigo-100 rounded-2xl w-full max-w-md shadow-xl p-6 transition-all hover:shadow-2xl">
      <!-- 标题区域（替换原 legend，更醒目） -->
      <div class="text-center mb-6">
        <h2 class="text-2xl font-bold bg-gradient-to-r from-indigo-600 to-purple-600 bg-clip-text text-transparent">
          欢迎回来
        </h2>
        <p class="text-sm text-gray-500 mt-1">请登录您的账号</p>
      </div>

      <!-- 用户名 -->
      <label class="label">
        <span class="label-text font-medium text-gray-700">用户名</span>
      </label>
      <input
        type="text"
        class="input input-bordered w-full rounded-lg border-gray-200 focus:border-indigo-300 focus:ring-2 focus:ring-indigo-200 transition-all"
        placeholder="请输入用户名"
      />

      <!-- 密码 -->
      <label class="label mt-4">
        <span class="label-text font-medium text-gray-700">密码</span>
      </label>
      <input
        type="password"
        class="input input-bordered w-full rounded-lg border-gray-200 focus:border-indigo-300 focus:ring-2 focus:ring-indigo-200 transition-all"
        placeholder="请输入密码"
      />

      <!-- 登录按钮 -->
      <button class="btn mt-6 w-full bg-gradient-to-r from-indigo-600 to-purple-600 text-white border-none hover:from-indigo-700 hover:to-purple-700 shadow-md hover:shadow-lg transition-all duration-200 rounded-lg py-3 text-base font-medium">
        登 录
      </button>

      <!-- 注册链接区域 -->
      <div class="flex items-center mt-4 text-sm">
        <RouterLink
          :to="{name:'user-account-register-index'}"
          class="ml-auto text-indigo-600 hover:text-indigo-800 hover:underline transition-colors font-medium"
        >
          注册新账号
        </RouterLink>
      </div>
    </fieldset>
  </div>

</template>

<style scoped>

</style>