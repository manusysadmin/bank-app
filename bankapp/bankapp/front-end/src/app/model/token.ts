export class Token {
  token: string;
  tokenExpires: Date;
  username: string;

  constructor() {
    this.token = '';
    this.tokenExpires = null;
    this.username = '';
  }
}
