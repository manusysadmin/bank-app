import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { LoginComponent } from './components/login/login.component';
import { ProductListComponent } from './components/product-list/product-list.component';
import { RegisterComponent } from './components/register/register.component';
import { ProductAddComponent } from './components/product-add/product-add.component';
import { AuthGuard } from './guards/auth.guard';


const routes: Routes = [
  { path: 'api/login', component: LoginComponent },
  { path: 'api/register', component: RegisterComponent },
  { path: 'api/products', component: ProductListComponent },
  { path: 'api/manage/add', component: ProductAddComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
