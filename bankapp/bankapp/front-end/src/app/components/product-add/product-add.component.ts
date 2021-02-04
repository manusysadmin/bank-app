import { Component, OnInit } from '@angular/core';
import { ProductService } from '../../services/product.service';
import {FormBuilder, FormGroup, Validators} from '@angular/forms';
import { Product } from '../../model/product';

@Component({
  selector: 'app-product-add',
  templateUrl: './product-add.component.html',
  styleUrls: ['./product-add.component.scss']
})
export class ProductAddComponent {

  public product: Product | undefined;
  productForm: FormGroup;
  message: null;
  public ageBrackets = {
    '0-17': 'JUNIOR',
    '18-64': 'ADULT',
    '65+': 'SENIOR'
  };
  public incomeBrackets = {
    ' 0 ': 'NO_INCOME',
    '1-12000': 'LOW_INCOME',
    '12001-40000': 'MEDIUM_INCOME',
    '40000+': 'HIGH_INCOME'
  };

  constructor(private productService: ProductService,
              private fb: FormBuilder) {
    this.initializeProduct();
    this.productForm = this.fb.group({
      name: ['', Validators.required],
      ageBracket: ['', Validators.required],
      incomeBracket: ['', Validators.required],
      student: ['', Validators.required]
    });
  }

  initializeProduct(): any {
    this.product = {
      name: '',
      age: '',
      student: false,
      income: '',
      slug: '',
    };
  }

  createProduct(productForm: any): any {
    if (productForm.valid) {
      this.productService.create(this.product)
        .subscribe((result: any) => {
          this.message = result.msg;
          this.initializeProduct();
        }, (err) => {
          this.message = err.error.msg;
        });
    } else {
      console.error('Product form is invalid.');
    }
  }
  get name(): any {
    return this.productForm.get('name');
  }
  get ageBracket(): any {
    return this.productForm.get('ageBracket');
  }
  get incomeBracket(): any {
    return this.productForm.get('incomeBracket');
  }
  get student(): any {
    return this.productForm.get('student');
  }
}
