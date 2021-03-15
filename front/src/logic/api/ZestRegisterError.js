import { ZestError } from './ZestError';

/**
 * Error Register
 *
 * @author Lucas Fridez <lucas.fridez@he-arc.ch>
 * @export
 * @class ZestRegisterError
 * @extends {ZestError}
 */
export class ZestRegisterError extends ZestError {

    /**
     * Creates an instance of ZestRegisterError.
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