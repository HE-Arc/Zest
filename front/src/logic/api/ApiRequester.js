//import store from '@/store';
import Axios /*,{ AxiosInstance, AxiosRequestConfig, AxiosResponse }*/ from "axios";
import { ZestError } from "./ZestError";
import { ZestError422 } from "./ZestError422";
import store from "../../store/index";

/**
 * API Service to link Front-End and Back-End
 * Allow developer to contact an APi with a Singleton pattern
 *
 * @author Lucas Fridez <lucas.fridez@he-arc.ch>
 * @class ApiRequester
 */
class ApiRequester {
  // Properties
  static singleton;
  instanceAxios;
  token;
  URL = "http://localhost:8000/";

  /**
   * Creates an instance of ApiRequester.
   * @author Lucas Fridez <lucas.fridez@he-arc.ch>
   */
  constructor() {
    this.token = null;
    this.instanceAxios = Axios.create({
      baseURL: `${this.URL}`,
      headers: {
        "Content-Type": "application/json",
        Accept: "application/json",
      },
    });
  }

  /**
   * Get Url
   *
   * @author Lucas Fridez <lucas.fridez@he-arc.ch>
   * @return {*}
   */
  getUrl() {
    return this.URL;
  }

  /**
   * Get ApiRequester Instance (or create it if inexistant)
   *
   * @author Lucas Fridez <lucas.fridez@he-arc.ch>
   * @readonly
   * @static
   * @type {ApiRequester}
   */
  static get instance() {
    if (!ApiRequester.singleton) {
      this.singleton = new ApiRequester();
    }

    return ApiRequester.singleton;
  }

  setToken(token) {
    this.token = token;
  }

  /**
   * Log User in Application and store his token
   *
   * @author Lucas Fridez <lucas.fridez@he-arc.ch>
   * @param {*} credentials credentials to log
   * @return {*}  {Promise<*>} API Response
   */
  async login(credentials) {
    try {
      const response = await this.instanceAxios.post("api/token/", credentials);

      //TODO
      this.token = response.data.access;
      const user = response.data.user;

      store.dispatch("login", { token: this.token, user: user });
      return response.data;
    } catch (error) {
      const data = error.response.data;
      if (error.response.status === 401) {
        throw new ZestError(data.code, data.detail, data.status);
      } else if (data.data == undefined) {
        throw new ZestError(data.code, data.message, data.status);
      } else {
        throw new ZestError422(data.code, data.message, data.status, data.data);
      }
    }
  }

  async logout() {
    store.dispatch("logout");
    this.token = null;
  }

  /**
   * Register an Account
   *
   * @author Lucas Fridez <lucas.fridez@he-arc.ch>
   * @param {*} account account to register
   * @return {*}  {Promise<AxiosResponse>} API Response
   */
  async register(account) {
    try {
      await this.instanceAxios.post("users", account);
      this.login({username: account.username, password: account.password});
    } catch (error) {
      const data = error.response.data;
      if (data.data == undefined) {
        throw new ZestError(data.code, data.message, data.status);
      } else {
        throw new ZestError422(data.code, data.message, data.status, data.data);
      }
    }
  }

  /**
   * Check if API server is UP
   *
   * @author Lucas Fridez <lucas.fridez@he-arc.ch>
   * @return {*}  {Promise<AxiosResponse>} API Response
   */
  getStateServer() {
    return this.instanceAxios.get("state");
  }

  /**
   * Request a GET Method
   *
   * @author Lucas Fridez <lucas.fridez@he-arc.ch>
   * @template T type to cast the data got from API
   * @param {string} url url to request
   * @return {*}  {Promise<T>} Promise of type T
   */
  async get(url) {
    try {
      const response = await this.instanceAxios.get(url, {
        headers: { Authorization: `Bearer ${this.token}` },
      });
      return response.data;
    } catch (error) {
      const data = error.response.data;
      if (data.data == undefined) {
        throw new ZestError(data.code, data.message, data.status);
      } else {
        throw new ZestError422(data.code, data.message, data.status, data.data);
      }
    }
  }

  /**
   * Request the API
   *
   * @author Lucas Fridez <lucas.fridez@he-arc.ch>
   * @private
   * @param {("GET" | "POST" | "PUT" | "DELETE" | "PATCH")} method string method to use
   * @param {string} url url to request
   * @param {*} [body] body to add in request
   * @return {*}  {Promise<*>} Api Response
   */
  async request(method, url, body) {
    const requestConfig = {
      method: method,
      url: url,
      headers: { Authorization: `Bearer ${this.token}` },
    };

    if (body) {
      requestConfig.data = body;
    }

    try {
      const response = await this.instanceAxios(requestConfig);
      return response.data;
    } catch (error) {
      const data = error.response.data;
      if (data.data == undefined) {
        throw new ZestError(data.code, data.message, data.status);
      } else {
        throw new ZestError422(data.code, data.message, data.status, data.data);
      }
    }
  }

  /**
   * POST data to API
   *
   * @author Lucas Fridez <lucas.fridez@he-arc.ch>
   * @param {string} url url to request
   * @param {*} body body to post
   * @return {*}  {Promise<*>} API Response
   */
  async post(url, body) {
    return this.request("POST", url, body);
  }

  /**
   * PUT data to API
   *
   * @author Lucas Fridez <lucas.fridez@he-arc.ch>
   * @param {string} url url to request
   * @param {*} body body to put
   * @return {*}  {Promise<*>} API Response
   */
  async put(url, body) {
    return this.request("PUT", url, body);
  }

  /**
   * DELETE method to API
   *
   * @author Lucas Fridez <lucas.fridez@he-arc.ch>
   * @param {string} url url to request
   * @return {*}  {Promise<*>} API Response
   */
  delete(url) {
    return this.request("DELETE", url);
  }

  /**
   * PATCH method to API
   *
   * @author Lucas Fridez <lucas.fridez@he-arc.ch>
   * @param {string} url url to request
   * @param {*} body body to PATCH
   * @return {*}  {Promise<*>} API Response
   */
  async patch(url, body) {
    return this.request("PATCH", url, body);
  }
}

export default ApiRequester.instance;
