import { Component, OnInit } from '@angular/core';
import { ProductService } from '../../services/product.service';

import {FormBuilder, FormControl, FormGroup, Validators} from '@angular/forms';

@Component({
  selector: 'app-product-list',
  templateUrl: './product-list.component.html',
  styleUrls: ['./product-list.component.scss']
})
export class ProductListComponent {

  queryForm: FormGroup;
  products: any;

  constructor(private productService: ProductService,
              private fb: FormBuilder) {
    this.queryForm = this.fb.group({
      ageBracket: ['', Validators.required],
      incomeBracket: ['', Validators.required],
      student: ['', Validators.required]
    });
  }

  get ageBracket() { return this.queryForm.get('ageBracket'); }
  get incomeBracket() { return this.queryForm.get('incomeBracket'); }
  get student() { return this.queryForm.get('student'); }
}
