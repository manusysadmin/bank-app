import { Component } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { AuthService } from '../../services/auth.service';
import { Router } from '@angular/router';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.scss']
})
export class LoginComponent {
  error: any;
  constructor(private authService: AuthService,
              private router: Router) {
  }

  login(username: string, password: string): any {
    this.authService.login(username, password).subscribe(
      (success: any) => this.router.navigate(['api/products']),
        (error: any) => {console.error(error); }
    );
  }
  // loginForm: FormGroup;
  //
  // constructor(private authService: AuthService,
  //             private fb: FormBuilder) {
  //   this.loginForm = this.fb.group({
  //     username: ['', Validators.required],
  //     password: ['', Validators.required]
  //   });
  // }
}
