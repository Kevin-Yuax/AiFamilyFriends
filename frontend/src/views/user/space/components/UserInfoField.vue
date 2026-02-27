<script setup>

defineProps(['userProfile'])

</script>

<template>
  <div v-if="userProfile" class="flex justify-center mt-12 px-4">
    <div class="flex flex-col md:flex-row gap-8 items-center md:items-start">
        <!-- 头像区域 -->
      <div class="avatar">
        <div class="w-36 md:w-44 rounded-full ring-4 ring-indigo-200/60 ring-offset-2 ring-offset-white shadow-lg">
          <img :src="userProfile.photo" alt="" class="object-cover w-full h-full rounded-full" />
        </div>
      </div>

      <!-- 文本信息区域 -->
      <div class="flex flex-col justify-center flex-1 text-center md:text-left space-y-2">
        <!-- 用户名 + 可能的徽章（可选） -->
        <div class="flex items-center justify-center md:justify-start gap-2">
          <div class="text-2xl font-bold text-gray-900 line-clamp-1 break-all">
            {{ userProfile.username }}
          </div>
          <!-- 可以放一个认证徽章，如果没有就省略 -->
        </div>

        <!-- AIFriends号 + 图标，使用更简洁的样式 -->
        <div class="flex items-center justify-center md:justify-start gap-1 text-sm text-gray-500">
          <svg xmlns="http://www.w3.org/2000/svg" class="h-4 w-4" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="1.5">
            <path stroke-linecap="round" stroke-linejoin="round" d="M15.75 6a3.75 3.75 0 11-7.5 0 3.75 3.75 0 017.5 0zM4.501 20.118a7.5 7.5 0 0114.998 0A17.933 17.933 0 0112 21.75c-2.676 0-5.216-.584-7.499-1.632z" />
          </svg>
          <span>AIFriends号：{{ userProfile.user_id }}</span>
        </div>

        <!-- 简介卡片：白底灰框，更清晰 -->
        <div class="w-72 bg-white border border-gray-200 rounded-xl p-1.5 text-gray-700 text-base leading-relaxed shadow-sm line-clamp-3">
          {{ userProfile.profile }}
        </div>
      </div>
    </div>


  </div>
</template>

<style scoped>
/* 确保头像图片完全覆盖圆形区域 */
.avatar .rounded-full img {
  object-fit: cover;
  width: 100%;
  height: 100%;
}

/* 可选：为卡片增加微妙的背景光晕 */
.bg-white {
  background: radial-gradient(circle at 10% 20%, rgba(255, 255, 255, 0.9) 0%, white 90%);
}
.profile-bio {
  /* 固定宽度，确保每行字符数稳定。根据设计调整，例如 16rem 或 20rem */
  width: 18rem;

  /* 多行省略核心 */
  display: -webkit-box;
  -webkit-line-clamp: 3;      /* 强制 3 行，超出省略 */
  -webkit-box-orient: vertical;
  overflow: hidden;

  /* 确保文本正常换行，不强制断单词，也不阻止换行 */
  word-break: normal;
  white-space: normal;

  /* 增加一点容错，防止其他样式覆盖 */
  max-height: none !important; /* 避免其他 max-height 干扰 */
}
</style>