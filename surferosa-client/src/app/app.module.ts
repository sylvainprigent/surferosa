import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import {NgbModule} from '@ng-bootstrap/ng-bootstrap';
import { AngularFontAwesomeModule } from 'angular-font-awesome';
import { FormsModule }   from '@angular/forms';

import { HttpClientModule, HTTP_INTERCEPTORS }    from '@angular/common/http';
import { TokenInterceptor} from './auth/token.interceptor';

import { AppComponent } from './app.component';
import { NavbarComponent } from './navbar/navbar.component';
import { NewsfeedComponent } from './newsfeed/newsfeed/newsfeed.component';
import { NewsComponent } from './newsfeed/news/news.component';
import { TopicsComponent } from './newsfeed/topics/topics.component';
import { NewspageComponent } from './newsfeed/newspage/newspage.component';
import { ToolshedBarComponent } from './toolshed/toolshed-bar/toolshed-bar.component';
import { MessagesComponent } from './messages/messages.component';
import { AppRoutingModule } from './/app-routing.module';
import { ChatComponent } from './chat/chat/chat.component';
import { LoginComponent } from './auth/login/login.component'

@NgModule({
  declarations: [
    AppComponent,
    NavbarComponent,
    NewsfeedComponent,
    NewsComponent,
    TopicsComponent,
    NewspageComponent,
    ToolshedBarComponent,
    MessagesComponent,
    ChatComponent,
    LoginComponent
  ],
  imports: [
    BrowserModule,
    NgbModule,
    AngularFontAwesomeModule,
    HttpClientModule,
    FormsModule,
    AppRoutingModule
  ],
  providers: [
    {
      provide: HTTP_INTERCEPTORS,
      useClass: TokenInterceptor,
      multi: true
    }
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
