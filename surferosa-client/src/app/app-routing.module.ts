import { NgModule }             from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { NewspageComponent }      from './newsfeed/newspage/newspage.component';
import { ChatComponent }      from './chat/chat/chat.component';

const routes: Routes = [
  { path: '', component: NewspageComponent },
  { path: 'newsfeed', component: NewspageComponent },
  { path: 'chat', component: ChatComponent }
];

@NgModule({
  imports: [ RouterModule.forRoot(routes) ],
  exports: [ RouterModule ]
})
export class AppRoutingModule {}
