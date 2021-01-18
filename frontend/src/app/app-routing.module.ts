import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';

import { HomeComponent } from './components/home/home.component';
import { LoginComponent } from './components/login/login.component';
import { ProductAddComponent } from './components/product-add/product-add.component';
import { ProductListComponent} from './components/product-list/product-list.component';
import { RegisterComponent } from './components/register/register.component';
import { ProductEditComponent } from './components/product-edit/product-edit.component';

const routes: Routes = [
  { path: '', redirectTo: 'products' },
  { path: 'login', component: LoginComponent },
  { path: 'register', component: RegisterComponent },
  { path: 'products', component: ProductListComponent },
  { path: 'products/manage/add', component: ProductAddComponent },
  { path: 'products/manage/:slug', component: ProductEditComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
