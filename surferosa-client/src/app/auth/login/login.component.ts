import { Component, OnInit } from '@angular/core';
import { Login } from '../login';
import { AuthService } from '../auth.service'
import { first } from 'rxjs/operators';
import { Router, ActivatedRoute } from '@angular/router';
import { MessagesService } from '../../messages/messages.service';

@Component({
  selector: 'app-chat',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

  constructor(private authService: AuthService,
    private router: Router,
    private route: ActivatedRoute,
    private messagesService: MessagesService) { }

  ngOnInit() {
    this.authService.logout();
    this.returnUrl = this.route.snapshot.queryParams['returnUrl'] || '/';
  }

  returnUrl: string;
  model = new Login("", "");

  submitted = false;

  onSubmit() {
    this.submitted = true;

    this.authService.login(this.model.username, this.model.password)
      .pipe(first())
      .subscribe(
        data => {
          this.router.navigate([this.returnUrl]);
        },
        error => {
          this.messagesService.add(error);
        });
  }

  // TODO: Remove this when we're done
  get diagnostic() { return JSON.stringify(this.model); }

}
