/**
 * Toudoum API Error
 *
 * @author Lucas Fridez <lucas.fridez@he-arc.ch>
 * @export
 * @class ZestError
 * @extends {Error}
 */
export class ZestError extends Error {
    // Properties
    code;
    status;

    /**
     * Creates an instance of ZestError.
     * @author Lucas Fridez <lucas.fridez@he-arc.ch>
     * @param {number} code Error code in Back-Office
     * @param {string} message Message sent from server
     * @param {number} status Http Response statusCode
     */
    constructor(code, message, status) {
        super(message);

        this.code = code;
        this.message = message;
        this.status = status;
    }
}