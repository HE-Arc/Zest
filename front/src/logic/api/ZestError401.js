import { ZestError } from './ZestError';

/**
 * Error 422 (When data error occured) like duplicate or missing parameters
 *
 * @author Lucas Fridez <lucas.fridez@he-arc.ch>
 * @export
 * @class ZestError422
 * @extends {ZestError}
 */
export class ZestError401 extends ZestError {
    data;

    /**
     * Creates an instance of ZestError422.
     * @author Lucas Fridez <lucas.fridez@he-arc.ch>
     * @param {number} code Error code in Back-Office
     * @param {string} message Message sent from server
     * @param {number} status Http Response statusCode 
     * @param {Array<any>} data data given from error
     */
    constructor(code, message, status) {
        super(code, message, status);

        this.code = code;
        this.message = message;
        this.status = status;
    }
}