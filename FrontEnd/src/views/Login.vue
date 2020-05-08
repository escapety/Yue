<template>
  <div>
    <div class="center">
      <img src="../assets/logo.png" height="250" width="250"/>
    </div>
    <el-row>
      <el-col :span="10" :offset="7">
        <el-tabs value="login" type="border-card" stretch>
          <el-tab-pane label="登录" name="login">
            <LoginForm/>
          </el-tab-pane>
          <el-tab-pane label="注册" name="register">
            <RegisterForm/>
          </el-tab-pane>
        </el-tabs>
      </el-col>
    </el-row>
  </div>
</template>
<script>
import LoginForm from '@/components/LoginForm'
import RegisterForm from '@/components/RegisterForm'
export default {
  components: {
    LoginForm,
    RegisterForm
  }
}
</script>
<style>
.center{
    display: flex;
    justify-content: center;
    align-items: center;
  }
</style>
