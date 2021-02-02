import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import {HTTP_INTERCEPTORS, HttpClientModule, HttpClientXsrfModule} from '@angular/common/http';
import { ReactiveFormsModule } from '@angular/forms';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { LoginComponent } from './components/login/login.component';
import { ProductAddComponent } from './components/product-add/product-add.component';
import {ProductService} from './services/product.service';
import {AuthService} from './services/auth.service';
import {TokenStorageService} from './services/token-storage.service';
import { ProductListComponent } from './components/product-list/product-list.component';
import { RegisterComponent } from './components/register/register.component';
import {HttpXsrfInterceptorService} from './services/http-xsrf-interceptor.service';

@NgModule({
  declarations: [
    AppComponent,
    LoginComponent,
    ProductAddComponent,
    ProductListComponent,
    RegisterComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
    ReactiveFormsModule,
    HttpClientXsrfModule.withOptions({
      cookieName: 'CSRF'
    })
  ],
  providers: [
    ProductService,
    AuthService,
    TokenStorageService,
    { provide: HTTP_INTERCEPTORS, useClass: HttpXsrfInterceptorService, multi: true }
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }

//TODO: add api to main route
//TODO: fix product list URL
//TODO: change list content type to JSON
