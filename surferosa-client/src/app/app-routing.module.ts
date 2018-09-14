import { NgModule }             from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

import { LoginComponent }      from './auth/login/login.component';
import { AuthGuard }      from './auth/auth.guard';

import { NewspageComponent }      from './newsfeed/newspage/newspage.component';
import { ChatComponent }      from './chat/chat/chat.component';


const routes: Routes = [
  { path: '', component: NewspageComponent, canActivate: [AuthGuard] },
  { path: 'login', component: LoginComponent }, 
  { path: 'newsfeed', component: NewspageComponent, canActivate: [AuthGuard]},
  { path: 'chat', component: ChatComponent, canActivate: [AuthGuard] }
  
];

@NgModule({
  imports: [ RouterModule.forRoot(routes) ],
  exports: [ RouterModule ]
})
export class AppRoutingModule {}
