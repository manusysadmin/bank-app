import { Component } from '@angular/core';
import { AuthService } from '../../services/auth.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.scss']
})
export class RegisterComponent {

  // public username: string;
  // public password: string = '';
  //
  // public message: string = '';
  // constructor(private userService: AuthService,
  //             private router: Router) { }

  // register() {
  //   this.userService.register(this.username, this.password)
  //     .subscribe((resp) => {
  //       console.log('Successfully registered');
  //       this.message = resp.msg;
  //       this.router.navigate(['login']);
  //     }, (err) => {
  //       console.error('Registration error', err);
  //     });
  // }

}
